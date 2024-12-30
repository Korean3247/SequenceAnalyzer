# SequenceAnalyzer

#### **Program Title**  
**RNA to Protein Sequence Translator**

#### **Description**  
This Python program translates a given RNA nucleotide sequence into its corresponding protein sequence by mapping codons to amino acids based on the standard genetic code. It includes input validation for start and stop codons and ensures proper sequence formatting.

#### **How It Works**  
1. The program prompts the user to input:  
   - A **start codon** (must be `AUG`).  
   - An RNA nucleotide sequence (in multiples of 3).  
   - A **stop codon** (one of `UAA`, `UAG`, or `UGA`).  

2. It validates the inputs by checking:  
   - The presence of a correct start codon.  
   - The presence of a valid stop codon.  
   - That the RNA sequence is a multiple of 3 and does not include the start or stop codons.

3. The program translates the RNA sequence into a protein sequence by matching codons to their respective amino acids using a predefined codon table. If an unknown codon is encountered, it labels it as "Unknown".

4. Finally, the resulting protein sequence is displayed.

#### **Input Requirements**  
- **Start Codon:** `AUG` (mandatory).  
- **RNA Sequence:** A string of RNA bases (`A`, `U`, `G`, `C`) in multiples of 3, excluding start and stop codons.  
- **Stop Codon:** One of `UAA`, `UAG`, or `UGA` (mandatory).  

#### **Features**  
- Built-in codon-to-amino acid mapping.  
- Validates input to prevent incorrect RNA sequences.  
- Detects and handles errors gracefully.  

#### **Usage Example**  
```plaintext
개시 코돈을 입력하세요: AUG  
RNA 염기서열을 입력하세요 (3배수로 입력): UUUCUUUAACGUA  
종결 코돈을 입력하세요: UAA  
아미노산 서열: 페닐알라닌 류신 아스파라진 발린
```

#### **Files**  
- **translate_sequence.py**: The main program file.  
- **README.txt**: This documentation file.

#### **System Requirements**  
- Python 3.x installed on your system.  
- A terminal or Python IDE to run the script.

#### **How to Run**  
1. Open a terminal or Python IDE.  
2. Run the script:  
   ```bash
   python translate_sequence.py
   ```
   
