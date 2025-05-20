qa_extraction_prompt = """
You are a software architecture assistant. From the following project documentation, extract all mentioned or implied software quality attributes. Examples include scalability, performance, modifiability, reliability, etc.

Please return a json list of the quality attributes as attributes along with detailed associated description from the documentation.

"""

design_decision_extraction_prompt = """
You are a software architecture assistant. From the following project documentation, extract all mentioned architectural design decisions.
Identify architectural design decisions, including rationale and any considered alternatives.

"""


qa_extraction_prompt_2 = """
You are an expert software architecture evaluator.

From the following context, extract a list of quality attributes (non-functional requirements) that are mentioned or implied. 
Each attribute should include:
- The name of the quality attribute
- A short description (one sentence) explaining why it is relevant based on the context
- The sustainability dimensions (Economic, Environmental, Social, Technical) impacted by this QA. For each dimension you list, include a short justification.

Respond in JSON format as follows:
[
  {{
    "attribute": "AttributeName",
    "description": "Short explanation of its relevance based on the context"
    
  }},
  ...
]

"""

qa_extraction_prompt_3 = """
You are an expert in software architecture and sustainability assessment.

Given the following software architecture documentation or design-related text, extract all the Quality Attributes (QAs) mentioned or implied.

For each QA you extract, provide the following:
1. QA Name – The name of the quality attribute (e.g., Availability, Modifiability).
2. Definition – A brief explanation in your own words based on the context.
3. Sustainability Dimensions – Identify which sustainability dimensions (Economic, Environmental, Social, Technical) are impacted by this QA. For each dimension you list, include a short justification.

Return the result as a JSON list in the following format:

[
  {{
    "qa": "Modifiability",
    "definition": "The ease with which the software architecture can accommodate changes.",
    "sustainability_dimensions": [
      {{
        "dimension": "Technical",
        "justification": "Supports long-term maintainability and architectural evolution."
      }},
      {{
        "dimension": "Economic",
        "justification": "Reduces cost of adapting the system over time."
      }}
    ]
  }},
  ...
]

Use only the information relevant to software quality attributes. If a sustainability dimension does not apply, do not include it.
"""

qa_extraction_prompt_4 = """
You are an expert in software architecture and sustainability assessment.

Given the following software architecture documentation or design-related text, extract all the Quality Attributes (QAs) that are mentioned or implied in the context.

For each extracted QA, provide:

1. QA Name – The name of the quality attribute (e.g., Availability, Modifiability).
2. Definition – A short explanation of the QA as it is understood or applied within the context of the provided text. Avoid generic or textbook-style definitions.
3. Sustainability Dimensions – Identify which sustainability dimensions (Economic, Environmental, Social, Technical) are impacted by this QA within the context of the document. For each dimension, provide a brief justification grounded in the content — explain how and why this QA influences that dimension based on the document.

Return the result as a JSON list using this format:

[
  {{
    "qa": "Modifiability",
    "definition": "In this context, it refers to how easily the integration between Canvas and institutional systems can be changed when the policy updates.",
    "sustainability_dimensions": [
      {{
        "dimension": "Technical",
        "justification": "Supports maintainability as the LMS integration will evolve over time."
      }},
      {{
        "dimension": "Economic",
        "justification": "Minimizes cost of future changes requested by policy or stakeholders."
      }}
    ]
  }}
]

Only include QAs that are contextually relevant. Do not invent QAs or sustainability impacts that are not evident in the text.
Respond only with the JSON.
"""

qa_extraction_prompt_5 = """
You are an expert in software architecture and sustainability evaluation.

Given the following software architecture documentation or design-related text, extract all the Quality Attributes (QAs) that are mentioned or strongly implied in the context.

For each extracted QA, provide:

1. QA Name – Use standard terminology (e.g., Availability, Modifiability, Security).
2. Definition – Explain the meaning of the QA as used or implied in the given document. Avoid generic definitions. Base your explanation on specific features, responsibilities, or architectural goals mentioned in the text.
3. Sustainability Dimensions – Identify which sustainability dimensions this QA impacts based only on what is written or clearly implied in the document. Choose from:
   - Economic
   - Environmental
   - Social
   - Technical

For each sustainability dimension you assign, provide a justification using explicit architectural mechanisms, design decisions, or technical details from the document.

If possible, quote or paraphrase small phrases from the document that support your justification. Your answer should be strictly tied to what is stated or implied in the document.

Return the output as a JSON array with the following structure:

[
  {{
    "qa": "Modifiability",
    "definition": "The architecture isolates jurisdiction-specific logic in separate modules, allowing rapid updates when laws change.",
    "sustainability_dimensions": [
      {{
        "dimension": "Technical",
        "justification": "The modular design facilitates localized changes, as mentioned in the 'System Decomposition' section."
      }},
      {{
        "dimension": "Economic",
        "justification": "Reduces engineering time needed for compliance updates."
      }}
    ]
  }},
  ...
]

Only include QAs that are relevant to the provided text. Do not include attributes or justifications that are not traceable to the document. Respond only with valid JSON.
"""



design_decision_extraction_prompt_2 ="""

You are an expert software architect. Analyze the architectural documentation and extract structured design decisions.

Each design decision should always strictly include:
1. Design Concern
2. Two Design Options
3. Rationale (per option)
4. Issues (if any)
5. Impacted Quality Attributes
6. Chosen Decision

Respond in the following JSON format:
[
  {{
    "design_concern": "string",
    "options": ["option 1", "option 2", ...],
    "rationale": {{
        "option 1": "reason 1",
        "option 2": "reason 2",
        ...
    }},
    "issues": ["issue 1", "issue 2"],
    "impacted_quality_attributes": ["Security", "Maintainability"],
    "chosen_decision": "selected option"
  }},
  ...
]
Return only valid JSON. Do not include any explanations, headings, or markdown.

"""

design_decision_extraction_prompt_3 = """
You are an expert in software architecture and sustainability-aware design evaluation.

Given the following architecture documentation or technical design text, extract all architectural design decisions.

For each design decision, provide the following fields:

1. Design Concern – The architectural problem, need, or constraint being addressed (e.g., deployment, data consistency, access control).
2. Options – Alternative solutions considered or implied.
3. Rationale – The reasoning or justification for each option, derived directly from the document (not general knowledge).
4. Issues – Any known or implied limitations, risks, or trade-offs associated with the options.
5. Supported Quality Attributes (QAs) – For each selected option, identify the QAs it impacts, organized by sustainability dimension:
   - Technical
   - Economic
   - Social
   - Environmental
6. Chosen Option – The selected or preferred option if it is clearly stated or implied.

Return your response as a valid JSON array using this structure:

[
  {{
    "design_concern": "string",
    "options": ["option 1", "option 2", ...],
    "rationale": {{
        "option 1": "reason 1",
        "option 2": "reason 2",
        ...
    }},
    "issues": ["issue 1", "issue 2"],
    "impacted_quality_attributes": ["Security", "Maintainability"],
    "chosen_decision": "selected option"
  }},
  ...
]

Return only valid JSON as your output. Do not include commentary, markdown, or explanations.
"""

tradeoff_prompt = """
You are a software architecture assistant evaluating trade-offs between two design options in a system.

Design Concern: Logging and Monitoring for Threat Detection

SIS (Sustainability Impact Score):
Centralized Logging with Anomaly Detection: 12
Decentralized Logging with Manual Audit: 9

These scores were calculated based on quality attribute impacts and their assigned priorities.

Quality Attribute Priorities (Higher means more important):
Security: 4
Responsiveness: 3
Recoverability: 2
Maintainability: 1

Option 1: Centralized Logging with Anomaly Detection

This option has the following impact relationships:

From Responsiveness:
  To Recoverability: +1
  To Maintainability: 0

From Recoverability:
  To Responsiveness: +1
  To Maintainability: +1

From Security:
  To Responsiveness: +1
  To Recoverability: +1
  To Maintainability: +1

Option 2: Decentralized Logging with Manual Audit

This option has the following impact relationships:

From Responsiveness:
  To Recoverability: +1
  To Maintainability: -1

From Recoverability:
  To Responsiveness: +1
  To Maintainability: -1

From Security:
  To Responsiveness: +1
  To Recoverability: +1
  To Maintainability: +1

Instructions:

Using the information above, write a clear and structured tradeoff analysis comparing the two design options.

Explain which quality attributes each option benefits or harms.
Take into account the quality attribute when explaining the tradeoff significance.
Highlight reasons why one might choose one option over the other, especially when priorities differ.
Use only the information provided.

"""
