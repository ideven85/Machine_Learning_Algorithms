import tensorflow as tf


class AttentionHead(tf.keras.layers.Layer):
    """
    using legacy
    """

    def __init__(self, d, H):
        super(AttentionHead, self).__init__()
        self.d_model = d  # e.g., 768
        self.H = H  # eg 12
        assert d % H == 0, "d should be divisible by heads"
        self.d_k = self.d_model // self.H  # 768/12=64
        # FUSED LINEAR LAYER: Projects input width into 3 * d_model space all at once
        self.qkv = tf.keras.layers.Dense(3 * self.d_model)

        # OUTPUT PROJECTION MATRIX (W_o): Collapses concatenated heads back to d_model
        self.W0 = tf.keras.layers.Dense(self.d_model)

    def call(self, x):
        # Input tensor shape: [Batch_Size, Seq_Len, d_model]
        batch_size = tf.shape(x)[0]
        seq_len = tf.shape(x)[1]
        qkv_tensor = self.qkv(x)

        # Step 1: Linear
        # projection
        # into
        # a
        # giant
        # fused
        # QKV
        # tensor
        # [Batch_Size, Seq_Len, d_model] -> [Batch_Size, Seq_Len, 3 * d_model]
        q, k, v = tf.split(qkv_tensor, 3, axis=-1)
        # Step 3: Reshape and permute axes to break d_model into [num_heads, d_key]
        # Target Shape for matching: [Batch_Size, num_heads, Seq_Len, d_key]

        def split_heads(tensor):
            tensor = tf.reshape(tensor, (batch_size, seq_len, self.H, self.d_k))
            return tf.transpose(tensor, perm=[0, 2, 1, 3])  # Swap axes 1 and 2

        q = split_heads(q)
        k = split_heads(k)
        v = split_heads(v)

        # Step 4: Scaled Dot-Product Attention Engine
        # Multiply Q by K Transposed along its last two axes (perm=[0, 1, 3, 2])
        # Shape of scores matrix: [Batch_Size, num_heads, Seq_Len, Seq_Len] -> Perfect Square!
        scores = tf.matmul(q, k, transpose_b=True) / tf.math.sqrt(
            tf.cast(self.d_k, tf.float32)
        )

        # Step 5: Softmax Normalization across the rows (last axis) to generate weights
        attention_weights = tf.nn.softmax(scores, axis=-1)

        # Step 6: Mix attention weights with Value vectors to compute Context matrix (Z)
        # Shape: [Batch_Size, num_heads, Seq_Len, d_key]
        z_heads = tf.matmul(attention_weights, v)

        # Step 7: Reassembly (Concatenation)
        # Transpose back to [Batch_Size, Seq_Len, num_heads, d_key] and collapse depth dimensions
        z_heads = tf.transpose(z_heads, perm=[0, 2, 1, 3])
        z_concatenated = tf.reshape(z_heads, (batch_size, seq_len, self.d_model))

        # Step 8: Multi-Head Assembly via W_o output matrix
        # Shape: [Batch_Size, Seq_Len, d_model]
        output = self.W0(z_concatenated)

        return output


def check():
    dummy_input = tf.random.normal([1, 4, 768])
    print(dummy_input.shape)


def main():
    seq_len = 4  # "To date, the cleverest"
    embedding_size = 126
    heads = 6

    # Instantiate custom TF layer block
    tf_attention_layer = AttentionHead(d=embedding_size, H=heads)

    # Pass dummy batch input through the computational tensor flow
    dummy_input = tf.random.normal([1, seq_len, embedding_size])
    print(f"Input Tensor Matrix Shape (X): {dummy_input.shape}")

    output_embeddings = tf_attention_layer(dummy_input)
    print(f"Output Embedding Matrix Shape (Z): {output_embeddings.shape}")


if __name__ == "__main__":
    main()
