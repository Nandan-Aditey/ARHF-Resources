# ARHF Prompts
This folder contains the prompts used in the **Ambiguity Resolution with Human Feedback (ARHF)** system, as described in our paper. ARHF is designed to detect and resolve ambiguities in natural language function specifications by leveraging CodeLLM generated test inputs, code, and incorporates human feedback into the system.

Overview of prompts used for each of the three key components of the system can be found below.

---

## Prompts Overview

| **Component**            | **Prompt Description** |
|--------------------------|------------------------|
| **Initial Code Generation** | Generates Python function code based on a natural language specification consisting of a signature, docstring, and doctests. |
| **Test Input Generation**   | Produces a list of input test cases to probe potential ambiguities in the given specification. |
| **Code Correction**         | Modifies buggy implementations based on failing doctests that clarify the intended behavior. |


