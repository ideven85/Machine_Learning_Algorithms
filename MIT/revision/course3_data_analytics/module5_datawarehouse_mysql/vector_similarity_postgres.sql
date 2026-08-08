CREATE EXTENSION vector;
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));

INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');
SELECT *
FROM items
ORDER BY embedding <-> '[3,1,2]'
LIMIT 5;

drop table items;
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
ALTER TABLE items ADD COLUMN embedding vector(3);

INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');

INSERT INTO items (id, embedding) VALUES (1, '[1,2,3]'), (2, '[4,5,6]')
ON CONFLICT (id) DO UPDATE SET embedding = EXCLUDED.embedding;

UPDATE items SET embedding = '[1,2,3]' WHERE id = 1;

SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;

--
-- Supported distance functions are:

-- <-> - L2 distance
-- <#> - (negative) inner product
-- <=> - cosine distance
-- <+> - L1 distance
-- <~> - Hamming distance (binary vectors)
-- <%> - Jaccard distance (binary vectors)

--

SELECT * FROM items WHERE id != 1 ORDER BY embedding <-> (SELECT embedding FROM items WHERE id = 1) LIMIT 5;

SELECT * FROM items WHERE embedding <-> '[3,1,2]' < 5;
-- Get the distance
SELECT embedding <-> '[3,1,2]' AS distance FROM items;

-- For inner product, multiply by -1 (since <#> returns the negative inner product)
SELECT (embedding <#> '[3,1,2]') * -1 AS inner_product FROM items;

-- Average vectors
select avg(items.embedding) from items;

-- group by average
CREATE INDEX ON items USING hnsw (embedding vector_l2_ops);
CREATE INDEX ON items USING hnsw (embedding vector_ip_ops);
CREATE INDEX ON items USING hnsw (embedding vector_cosine_ops);
CREATE INDEX ON items USING hnsw (embedding vector_l1_ops);

SELECT category_id, AVG(embedding) FROM items GROUP BY category_id;