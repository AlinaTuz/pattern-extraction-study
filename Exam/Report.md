# Murderer mystery

## Available Files:

1.  `murder_solution.ipynb` – The Jupyter Notebook containing all the analysis code and its description.

To run the notebook correctly, you need to install the following Python libraries:
You can install them using pip:
```bash
!pip install sentence-transformers scikit-learn networkx matplotlib
```

## Suspect Analysis Report

### Primary Suspect: Doctor Ashcroft 

**Several indicators point to Dr. Ashcroft as the main suspect:**

- Semantic Similarity to Murderer’s Note:
His statement shows the highest similarity score (0.4041) among all suspects when compared to the murderer's note, indicating potential authorship or strong alignment in phrasing and tone.

- Dialect Match Score:
He ranks among the top suspects with a dialect match score of 5, suggesting notable overlap with distinctive words and phrases found in the note.

- Witness Interactions:
He was seen by only 8 other guests, which is relatively few.
Importantly, he did not report seeing anyone himself, which may indicate an attempt to obscure his movements.

Multiple guests mentioned seeing someone who might have been Doctor Ashcroft, but none were certain. Phrases such as:

"I also think I saw Doctor Ashcroft, but I'm not entirely sure."

"Someone who might have been Doctor Ashcroft walked by quickly."

"I caught a glimpse of someone who looked like Doctor Ashcroft."

"I briefly saw Doctor Ashcroft passing by."

...suggest that his presence was vague and uncertain to others.

Furthermore, none of the witnesses mentioned receiving, writing, or seeing any note, reinforcing the idea that Doctor Ashcroft kept a low profile during the evening. His mention is rare and hesitant, indicating that people are unsure whether it was really him they saw. This ambiguity could point to a deliberate attempt to stay unnoticed—or to someone impersonating him.

- Clustering Analysis:
Dr. Ashcroft is the only member of Cluster 7, showing his statement is linguistically distinct from all others — a potential strange suggesting inconsistency or deception.

These combined factors make Doctor Ashcroft the most likely suspect based on the current linguistic and network evidence.

**Lord Green second suspect**

Lord Green also raises suspicion based on unusual social interaction data:

- Solitary Claim:
He stated that he “didn’t notice anyone”, placing him among guests who claimed to be alone.

- Contradictory Witness Reports:
Despite his claim, 8 different individuals reported seeing him, revealing a significant discrepancy and possible dishonesty.

- Moderate Semantic Similarity:
His similarity score to the murderer's note is 0.3614, which, while not the highest, places him within the top five.

## Conclusion:

While both individuals exhibit suspicious patterns, Doctor Ashcroft stands out due to his high linguistic match with the murderer's note and isolation across multiple analytical layers. Lord Green follows as a secondary suspect due to contradictions in reported interactions.

Further investigation should prioritize these two individuals.

---

Notes that were made:

--- Top Statements by Semantic Similarity to Murderer's Note ---

Guest: Doctor Ashcroft, Similarity: 0.4041 

Guest: Viscount Pemberton, Similarity: 0.3964

Guest: Baron Sienna, Similarity: 0.3910

Guest: Lord Green, Similarity: 0.3614

Guest: Inspector Ivory, Similarity: 0.3374

--- Suspects Ranked by Dialect Match Score (Higher is More Similar) ---

Guest: Baron Sienna (too many people saw)
  Score: 14

Guest: Counselor Montgomery (too many people saw)
  Score: 12

Guest: Inspector Ivory (too many people saw)
  Score: 10

Guest: Viscount Pemberton (18 people saw)
  Score: 8

Guest: Viscount Onyx (too many people saw)
  Score: 8

Guest: Brigadier Black (too many people saw)
  Score: 7

Guest: Doctor Ashcroft (8 people saw)
  Score: 5

--- Statements Grouped into 7 Clusters ---

Cluster 7: (1 members)
Doctor Ashcroft

--- Guests Claiming to See No One or Be Alone (Based on Expanded Phrase List) ---

GUEST: Lord Green

Claim Evidence: Matched phrase: 'didn't notice anyone' in statement.

ATTENTION: Reportedly seen by -> Ambassador Northbrook, Baron Nightingale, Brigadier Black, Duchess Summerville, General White, Mister Coral, Rector Sapphire, Solicitor Ravenscroft

--- One-Way Sightings (A saw B, but B didn't report seeing A): ---

Ambassador Beaumont but Ambassador Beaumont: Seen by 24 other(s)


Main Suspects:
1. Doctor Ashcroft
2. Lord Green