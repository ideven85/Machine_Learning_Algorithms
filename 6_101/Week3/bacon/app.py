import os
import pickle
from mcp.server.fastmcp import FastMCP
import lab

# 1. Initialize the FastMCP Framework Agent
mcp = FastMCP("MIT-6101-Bacon-Supervisor")

# 2. Maintain a global reference to the pre-loaded dictionary structures
DATABASES = {}
RESOURCES_DIR = os.path.join(os.path.dirname(__file__), "resources")


def ensure_dataset_loaded(size: str = "small"):
    """
    Ensures targeted data subsets ('tiny', 'small', 'large') are loaded and
    pre-transformed into memory adjacency dicts exactly once.
    """
    if size not in DATABASES:
        filename = os.path.join(RESOURCES_DIR, f"{size}.pickle")
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Pickle asset path missing at: {filename}")

        with open(filename, "rb") as f:
            raw_data = pickle.load(f)
            # Store the normalized transformed dictionary mapping in our state container
            DATABASES[size] = lab.transform_data(raw_data)
    return DATABASES[size]


# --- Exposing Lab Algorithms as AI Executive Tools ---


@mcp.tool()
async def find_actor_bacon_path(actor_id: int, dataset_size: str = "small") -> str:
    """
    Traces the shortest sequence of Actor IDs linking Kevin Bacon (4724) to the target actor.
    Useful for discovering degrees of separation.

    Args:
        actor_id: The unique ID number of the destination target actor.
        dataset_size: Choose 'tiny', 'small', or 'large' based on processing constraints.
    """
    try:
        graph = ensure_dataset_loaded(dataset_size)
        path = lab.bacon_path(graph, actor_id)
        if path is None:
            return f"No valid connection path exists between Kevin Bacon and Actor {actor_id}."
        return f"Shortest path mapped successfully: {path} (Length: {len(path) - 1} movies)"
    except Exception as e:
        return f"Execution Error parsing network: {str(e)}"


@mcp.tool()
async def get_actors_by_degree(degree: int, dataset_size: str = "small") -> str:
    """
    Gathers a collection of all Actor IDs containing an exact Bacon Number layer index.

    Args:
        degree: The exact integer number of movie separations from Kevin Bacon.
        dataset_size: Choose 'tiny', 'small', or 'large'.
    """
    try:
        graph = ensure_dataset_loaded(dataset_size)
        actor_set = lab.actors_with_bacon_number(graph, degree)
        # Convert set entries into a scannable, cleanly typed array list block
        actor_list = sorted(list(actor_set))
        return (
            f"Found {len(actor_list)} actors with an exact Bacon Number of {degree}.\n"
            f"Sample IDs: {actor_list[:30]}..."
        )
    except Exception as e:
        return f"Execution Error capturing degree sets: {str(e)}"


@mcp.tool()
async def evaluate_co_stars(
    actor_id_1: int, actor_id_2: int, dataset_size: str = "small"
) -> str:
    """
    Asserts a clean boolean evaluation checking if two actors ever appeared in the same movie.
    """
    try:
        graph = ensure_dataset_loaded(dataset_size)
        result = lab.acted_together(graph, actor_id_1, actor_id_2)
        return f"Co-star relationship state for {actor_id_1} and {actor_id_2}: {result}"
    except Exception as e:
        return f"Execution Error evaluating pairs: {str(e)}"


if __name__ == "__main__":
    # MCP standard protocol maps communications over input/output pipelines natively (stdio)
    mcp.run(transport="stdio")
