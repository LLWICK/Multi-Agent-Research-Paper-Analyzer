import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the path to the parent directory (one level up)
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to the system path
sys.path.append(parent_dir)

def multi_step_retrieval(retriever_tool):
    sections = {
        "Name": "Research paper Name",
        "Abstract": "abstract of the research paper with title",
        "Method": "methodology or algorithm used in the paper",
        "Math": "mathematical equations formulas and theory",
        "Experiments": "datasets experimental setup evaluation",
        "Results": "results performance evaluation findings"
    }

    results = {}

    for key, query in sections.items():
        result = retriever_tool.invoke(query)

        # Optional refinement (if weak result)
        if len(result) < 200:
            result += "\n" + retriever_tool.invoke(query + " in detail")

        results[key] = result

    return results

