nemonicos_computador_completo = {
"NOP": [[0x00], 1],
"CLC": [[0x40], 1], "CLV": [[0x50], 1],
"SEC": [[0xC0], 1], "SEV": [[0xD0], 1],

"CLR A": [[0x01], 1], "IN A": [[0x02], 1],  "NEG A": [[0x03], 1], "INV A": [[0x04], 1],
"INC A": [[0x43], 1], "DEC A": [[0x44], 1],
"AND A": [[0x05], 1], "OR A": [[0x06], 1],  "XOR A": [[0x07], 1],
"ADD A": [[0x08], 1], "SUB A": [[0x09], 1], "ADC A": [[0x0A], 1], "SBC A": [[0x0B], 1], "CMP A": [[0x0C], 1],
"ROD A": [[0x0D], 1], "ROI A": [[0x0E], 1],
"RCD A": [[0x4D], 1], "RCI A": [[0x4E], 1],
"DAD A": [[0x8D], 1], "DAI A": [[0x8E], 1],
"DLD A": [[0xCD], 1],

"CLR B": [[0x11], 1], "IN B": [[0x12], 1],  "NEG B": [[0x13], 1], "INV B": [[0x14], 1],
"INC B": [[0x53], 1], "DEC B": [[0x54], 1],
"ROD B": [[0x1D], 1], "ROI B": [[0x1E], 1],
"RCD B": [[0x5D], 1], "RCI B": [[0x5E], 1],
"DAD B": [[0x9D], 1], "DAI B": [[0x9E], 1],
"DLD B": [[0xDD], 1],

"CLR C": [[0x21], 1], "IN C": [[0x22], 1],  "NEG C": [[0x23], 1], "INV C": [[0x24], 1],
"INC C": [[0x63], 1], "DEC C": [[0x64], 1],
"ROD C": [[0x2D], 1], "ROI C": [[0x2E], 1],
"RCD C": [[0x6D], 1], "RCI C": [[0x6E], 1],
"DAD C": [[0xAD], 1], "DAI C": [[0xAE], 1],
"DLD C": [[0xED], 1],

"LDA A,B": [[0x51], 1],
"AND A,B": [[0x55], 1], "OR A,B": [[0x56], 1],  "XOR A,B": [[0x57], 1],
"ADD A,B": [[0x58], 1], "SUB A,B": [[0x59], 1], "ADC A,B": [[0x5A], 1], "SBC A,B": [[0x5B], 1], "CMP A,B": [[0x5C], 1],
"LDA A,C": [[0x61], 1],
"AND A,C": [[0x65], 1], "OR A,C": [[0x66], 1],  "XOR A,C": [[0x67], 1],
"ADD A,C": [[0x68], 1], "SUB A,C": [[0x69], 1], "ADC A,C": [[0x6A], 1], "SBC A,C": [[0x6B], 1], "CMP A,C": [[0x6C], 1],
"LDA B,A": [[0x91], 1],
"AND B,A": [[0x95], 1], "OR B,A": [[0x96], 1],  "XOR B,A": [[0x97], 1],
"ADD B,A": [[0x98], 1], "SUB B,A": [[0x99], 1], "ADC B,A": [[0x9A], 1], "SBC B,A": [[0x9B], 1], "CMP B,A": [[0x9C], 1],
"LDA B,C": [[0xA1], 1],
"AND B,C": [[0xA5], 1], "OR B,C": [[0xA6], 1],  "XOR B,C": [[0xA7], 1],
"ADD B,C": [[0xA8], 1], "SUB B,C": [[0xA9], 1], "ADC B,C": [[0xAA], 1], "SBC B,C": [[0xAB], 1], "CMP B,C": [[0xAC], 1],
"LDA C,A": [[0xD1], 1],
"AND C,A": [[0xD5], 1], "OR C,A": [[0xD6], 1],  "XOR C,A": [[0xD7], 1],
"ADD C,A": [[0xD8], 1], "SUB C,A": [[0xD9], 1], "ADC C,A": [[0xDA], 1], "SBC C,A": [[0xDB], 1], "CMP C,A": [[0xDC], 1],
"LDA C,B": [[0xE1], 1],
"AND C,B": [[0xE5], 1], "OR C,B": [[0xE6], 1],  "XOR C,B": [[0xE7], 1],
"ADD C,B": [[0xE8], 1], "SUB C,B": [[0xE9], 1], "ADC C,B": [[0xEA], 1], "SBC C,B": [[0xEB], 1], "CMP C,B": [[0xEC], 1],

"LDA A,M": [[0x71], 3], "STA A,M": [[0x72], 3],
"AND A,M": [[0x75], 3], "OR A,M": [[0x76], 3],  "XOR A,M": [[0x77], 3],
"ADD A,M": [[0x78], 3], "SUB A,M": [[0x79], 3], "ADC A,M": [[0x7A], 3], "SBC A,M": [[0x7B], 3], "CMP A,M": [[0x7C], 3],
"LDA B,M": [[0xB1], 3], "STA B,M": [[0xB2], 3],
"AND B,M": [[0xB5], 3], "OR B,M": [[0xB6], 3],  "XOR B,M": [[0xB7], 3],
"ADD B,M": [[0xB8], 3], "SUB B,M": [[0xB9], 3], "ADC B,M": [[0xBA], 3], "SBC B,M": [[0xBB], 3], "CMP B,M": [[0xBC], 3],
"LDA C,M": [[0xF1], 3], "STA C,M": [[0xF2], 3],
"AND C,M": [[0xF5], 3], "OR C,M": [[0xF6], 3],  "XOR C,M": [[0xF7], 3],
"ADD C,M": [[0xF8], 3], "SUB C,M": [[0xF9], 3], "ADC C,M": [[0xFA], 3], "SBC C,M": [[0xFB], 3], "CMP C,M": [[0xFC], 3],

"HLT": [[0x10], 1],

"INX": [[0x83], 1], "DEX": [[0x84], 1],
"INY": [[0x93], 1], "DEY": [[0x94], 1],
"INP": [[0xA3], 1], "DEP": [[0xA4], 1],

"LDX M": [[0xBF], 3], "STX M": [[0xB0], 3], #"CPX M": [[0x3F], 3],
"LDY M": [[0xFF], 3], "STY M": [[0xF0], 3], #"CPY M": [[0x7F], 3],
"LDP M": [[0xF3], 3], "STP M": [[0xF4], 3],

"LDX N": [[0x8F], 3], "CPX N": [[0x0F], 3],
"LDY N": [[0xCF], 3], "CPY N": [[0x4F], 3],
"LDP N": [[0xC3], 3],

"BRC M": [[0x15], 3], "BRV M": [[0x16], 3], "BRN M": [[0x17], 3], "BRZ M": [[0x18], 3], "BMA M": [[0x19], 3], "BMI M": [[0x1A], 3], "BME M": [[0x1B], 3], "BNI M": [[0x1C], 3],
"BNC M": [[0x25], 3], "BNV M": [[0x26], 3], "BRP M": [[0x27], 3], "BNZ M": [[0x28], 3], "BSU M": [[0x29], 3], "BSI M": [[0x2A], 3], "BIN M": [[0x2B], 3], "BII M": [[0x2C], 3],
"BRI M": [[0x35], 3], "BSR M": [[0x36], 3], "RET":   [[0x37], 1],

"CLR M": [[0x31], 3], "NEG M": [[0x33], 3], "INV M": [[0x34], 3],
"INC M": [[0x73], 3], "DEC M": [[0x74], 3],
"ROD M": [[0x3D], 3], "ROI M": [[0x3E], 3], "RCD M": [[0x7D], 3], "RCI M": [[0x7E], 3],
"DAD M": [[0xBD], 3], "DAI M": [[0xBE], 3], "DLD M": [[0xFD], 3],

"LDA A,N": [[0x41], 2],
"AND A,N": [[0x45], 2], "OR A,N" : [[0x46], 2], "XOR A,N": [[0x47], 2],
"ADD A,N": [[0x48], 2], "SUB A,N": [[0x49], 2], "ADC A,N": [[0x4A], 2], "SBC A,N": [[0x4B], 2], "CMP A,N": [[0x4C], 2],

"LDA B,N": [[0x81], 2],
"AND B,N": [[0x85], 2], "OR B,N" : [[0x86], 2], "XOR B,N": [[0x87], 2],
"ADD B,N": [[0x88], 2], "SUB B,N": [[0x89], 2], "ADC B,N": [[0x8A], 2], "SBC B,N": [[0x8B], 2], "CMP B,N": [[0x8C], 2],

"LDA C,N": [[0xC1], 2],
"AND C,N": [[0xC5], 2], "OR C,N" : [[0xC6], 2], "XOR C,N": [[0xC7], 2],
"ADD C,N": [[0xC8], 2], "SUB C,N": [[0xC9], 2], "ADC C,N": [[0xCA], 2], "SBC C,N": [[0xCB], 2], "CMP C,N": [[0xCC], 2],


"LDA A,IX": [[0x80, 0x01], 3], "STA A,IX": [[0x80, 0x02], 3],
"AND A,IX": [[0x80, 0x05], 3], "OR A,IX" : [[0x80, 0x06], 3], "XOR A,IX": [[0x80, 0x07], 3],
"ADD A,IX": [[0x80, 0x08], 3], "SUB A,IX": [[0x80, 0x09], 3], "ADC A,IX": [[0x80, 0x0A], 3], "SBC A,IX": [[0x80, 0x0B], 3], "CMP A,IX": [[0x80, 0x0C], 3],

"LDA B,IX": [[0x80, 0x11], 3], "STA B,IX": [[0x80, 0x12], 3],
"AND B,IX": [[0x80, 0x15], 3], "OR B,IX" : [[0x80, 0x16], 3], "XOR B,IX": [[0x80, 0x17], 3],
"ADD B,IX": [[0x80, 0x18], 3], "SUB B,IX": [[0x80, 0x19], 3], "ADC B,IX": [[0x80, 0x1A], 3], "SBC B,IX": [[0x80, 0x1B], 3], "CMP B,IX": [[0x80, 0x1C], 3],

"LDA C,IX": [[0x80, 0x21], 3], "STA C,IX": [[0x80, 0x22], 3],
"AND C,IX": [[0x80, 0x25], 3], "OR C,IX" : [[0x80, 0x26], 3], "XOR C,IX": [[0x80, 0x27], 3],
"ADD C,IX": [[0x80, 0x28], 3], "SUB C,IX": [[0x80, 0x29], 3], "ADC C,IX": [[0x80, 0x2A], 3], "SBC C,IX": [[0x80, 0x2B], 3], "CMP C,IX": [[0x80, 0x2C], 3],

"CLR IX": [[0x80, 0x41], 3], "NEG IX": [[0x80, 0x43], 3], "INV IX": [[0x80, 0x44], 3],
"INC IX": [[0x80, 0x53], 3], "DEC IX": [[0x80, 0x54], 3],
"ROD IX": [[0x80, 0x4D], 3], "ROI IX": [[0x80, 0x4E], 3], "RCD IX": [[0x80, 0x5D], 3], "RCI IX": [[0x80, 0x5E], 3],
"DAD IX": [[0x80, 0x6D], 3], "DAI IX": [[0x80, 0x6E], 3], "DLD IX": [[0x80, 0x7D], 3],

"LDX IX": [[0x80, 0x6F], 3], #"CPX IX": [[0x80, 0x4F], 3],
"LDY IX": [[0x80, 0x7F], 3], #"CPY IX": [[0x80, 0x5F], 3],
"LDP IX": [[0x80, 0x73], 3],


"LDA A,IY": [[0x80, 0x81], 3], "STA A,IY": [[0x80, 0x82], 3],
"AND A,IY": [[0x80, 0x85], 3], "OR A,IY" : [[0x80, 0x86], 3], "XOR A,IY": [[0x80, 0x87], 3],
"ADD A,IY": [[0x80, 0x88], 3], "SUB A,IY": [[0x80, 0x89], 3], "ADC A,IY": [[0x80, 0x8A], 3], "SBC A,IY": [[0x80, 0x8B], 3], "CMP A,IY": [[0x80, 0x8C], 3],

"LDA B,IY": [[0x80, 0x91], 3], "STA B,IY": [[0x80, 0x92], 3],
"AND B,IY": [[0x80, 0x95], 3], "OR B,IY" : [[0x80, 0x96], 3], "XOR B,IY": [[0x80, 0x97], 3],
"ADD B,IY": [[0x80, 0x98], 3], "SUB B,IY": [[0x80, 0x99], 3], "ADC B,IY": [[0x80, 0x9A], 3], "SBC B,IY": [[0x80, 0x9B], 3], "CMP B,IY": [[0x80, 0x9C], 3],

"LDA C,IY": [[0x80, 0xA1], 3], "STA C,IY": [[0x80, 0xA2], 3],
"AND C,IY": [[0x80, 0xA5], 3], "OR C,IY" : [[0x80, 0xA6], 3], "XOR C,IY": [[0x80, 0xA7], 3],
"ADD C,IY": [[0x80, 0xA8], 3], "SUB C,IY": [[0x80, 0xA9], 3], "ADC C,IY": [[0x80, 0xAA], 3], "SBC C,IY": [[0x80, 0xAB], 3], "CMP C,IY": [[0x80, 0xAC], 3],

"CLR IY": [[0x80, 0xC1], 3], "NEG IY": [[0x80, 0xC3], 3], "INV IY": [[0x80, 0xC4], 3],
"INC IY": [[0x80, 0xD3], 3], "DEC IY": [[0x80, 0xD4], 3],
"ROD IY": [[0x80, 0xCD], 3], "ROI IY": [[0x80, 0xCE], 3], "RCD IY": [[0x80, 0xDD], 3], "RCI IY": [[0x80, 0xDE], 3],
"DAD IY": [[0x80, 0xED], 3], "DAI IY": [[0x80, 0xEE], 3], "DLD IY": [[0x80, 0xFD], 3],

"LDX IY": [[0x80, 0xEF], 3], #"CPX IY": [[0x80, 0xCF], 3],
"LDY IY": [[0x80, 0xFF], 3], #"CPY IY": [[0x80, 0xDF], 3],
"LDP IY": [[0x80, 0xF3], 3]
}


instrucciones_arg = {
'CLR' : [['acumuladores', 'indexado', 'directo']],
'NOP' : [],
'HLT' : [],
'CLC' : [],
'CLV' : [],
'SEC' : [],
'SEV' : [],
'IN'  : [['acumuladores']],
'NEG' : [['acumuladores', 'indexado', 'directo']],
'INV' : [['acumuladores', 'indexado', 'directo']],
'INC' : [['acumuladores', 'indexado', 'directo']],
'DEC' : [['acumuladores', 'indexado', 'directo']],
'AND' : [['acumuladores'],['acumuladores', 'inmediato', 'indexado', 'directo']],
'OR'  : [['acumuladores'],['acumuladores', 'inmediato', 'indexado', 'directo']],
'XOR' : [['acumuladores'],['acumuladores', 'inmediato', 'indexado', 'directo']],
'ADD' : [['acumuladores'],['acumuladores', 'inmediato', 'indexado', 'directo']],
'SUB' : [['acumuladores'],['acumuladores', 'inmediato', 'indexado', 'directo']],
'ADC' : [['acumuladores'],['acumuladores', 'inmediato', 'indexado', 'directo']],
'SBC' : [['acumuladores'],['acumuladores', 'inmediato', 'indexado', 'directo']],
'CMP' : [['acumuladores'],['acumuladores', 'inmediato', 'indexado', 'directo']],
'LDA' : [['acumuladores'],['acumuladores', 'inmediato', 'indexado', 'directo']],
'STA' : [['acumuladores'],['indexado', 'directo']],
'ROD' : [['acumuladores', 'indexado', 'directo']],
'ROI' : [['acumuladores', 'indexado', 'directo']],
'RCD' : [['acumuladores', 'indexado', 'directo']],
'RCI' : [['acumuladores', 'indexado', 'directo']],
'DAD' : [['acumuladores', 'indexado', 'directo']],
'DAI' : [['acumuladores', 'indexado', 'directo']],
'DLD' : [['acumuladores', 'indexado', 'directo']],
'CPX' : [['inmediato']],
'CPY' : [['inmediato']],
'INX' : [],
'INY' : [],
'INP' : [],
'DEX' : [],
'DEY' : [],
'DEP' : [],
'LDX' : [['inmediato', 'directo']],
'LDY' : [['inmediato', 'directo']],
'LDP' : [['inmediato', 'directo']],
'STX' : [['indexado', 'directo']],
'STY' : [['indexado', 'directo']],
'STP' : [['indexado', 'directo']],
'BRC' : [['directo']],
'BNC' : [['directo']],
'BRV' : [['directo']],
'BNV' : [['directo']],
'BRN' : [['directo']],
'BRP' : [['directo']],
'BRZ' : [['directo']],
'BNZ' : [['directo']],
'BMA' : [['directo']],
'BSU' : [['directo']],
'BMI' : [['directo']],
'BSI' : [['directo']],
'BME' : [['directo']],
'BIN' : [['directo']],
'BNI' : [['directo']],
'BII' : [['directo']],
'BRI' : [['directo']],
'BSR' : [['directo']],
'RET' : []
}

def nemonicos_microsex():
    return dict(nemonicos_computador_completo)

def argumentos_instrucciones():
    return dict(instrucciones_arg)
