def translate_sequence(sequence):
    codon_table = {
        'UUU': '페닐알라닌', 'UUC': '페닐알라닌',
        'UUA': '류신', 'UUG': '류신',
        'CUU': '류신', 'CUC': '류신', 'CUA': '류신', 'CUG': '류신',
        'AUU': '이소류신', 'AUC': '이소류신', 'AUA': '이소류신', 'AUG': '메싸이오닌(개시 코돈)',
        'GUU': '발린', 'GUC': '발린', 'GUA': '발린', 'GUG': '발린',
        'UCU': '세린', 'UCC': '세린', 'UCA': '세린', 'UCG': '세린',
        'CCU': '프롤린', 'CCC': '프롤린', 'CCA': '프롤린', 'CCG': '프롤린',
        'ACU': '트레오닌', 'ACC': '트레오닌', 'ACA': '트레오닌', 'ACG': '트레오닌',
        'GCU': '알라닌', 'GCC': '알라닌', 'GCA': '알라닌', 'GCG': '알라닌',
        'UAU': '타이로신', 'UAC': '타이로신',
        'CAU': '히스티딘', 'CAC': '히스티딘', 'CAA': '글루타민', 'CAG': '글루타민',
        'AAU': '아스파라진', 'AAC': '아스파라진', 'AAA': '리신', 'AAG': '리신',
        'GAU': '아스파트산', 'GAC': '아스파트산', 'GAA': '글루탐산', 'GAG': '글루탐산',
        'UGU': '시스테인', 'UGC': '시스테인',
        'CGU': '아르지닌', 'CGC': '아르지닌', 'CGA': '아르지닌', 'CGG': '아르지닌',
        'AGU': '세린', 'AGC': '세린', 'AGA': '아르진닌', 'AGG': '아르진닌',
        'GGU': '글리신', 'GGC': '글리신', 'GGA': '글리신', 'GGG': '글리신',
        'UAA': '종결 코돈', 'UAG': '종결 코돈', 'UGA': '종결 코돈'
    }

    protein_sequence = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3].upper()
        if codon in codon_table:
            protein_sequence += codon_table[codon] + " "
        else:
            protein_sequence += "알 수 없음 "
    return protein_sequence.strip()

# 개시 코돈 입력
start_codon = input("개시 코돈을 입력하세요: ")
if start_codon != "AUG":
    print("오류: 올바른 개시 코돈인 'AUG'을 입력하세요.")
    exit()

# 염기서열 입력
sequence = input("RNA 염기서열을 입력하세요 (3배수로 입력): ")

# 종결 코돈 입력
stop_codon = input("종결 코돈을 입력하세요: ")
if stop_codon not in ["UAA", "UAG", "UGA"]:
    print("오류: 올바른 종결 코돈 중 하나인 'UAA', 'UAG', 'UGA'를 입력하세요.")
    exit()

# 개시 코돈과 종결 코돈이 염기 서열에 포함되어 있는지 확인
while start_codon in sequence or stop_codon in sequence:
    print("오류: 개시 코돈 또는 종결 코돈은 염기서열에 포함되면 안됩니다.")
    sequence = input("다시 RNA 염기서열을 입력하세요 (3배수로 입력): ")

# 입력된 염기서열의 아미노산 변환
if len(sequence) % 3 == 0:
    protein = translate_sequence(sequence)
    print("아미노산 서열:", protein)
else:
    print("오류: 3배수로 염기서열을 입력하세요.")