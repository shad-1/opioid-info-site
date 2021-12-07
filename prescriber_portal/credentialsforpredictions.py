credentials = [
'acnp',
'acnpbc',
'agacnp',
'anp',
'anpbc',
'anpc',
'apn',
'apnc',
'apnp',
'aprn',
'aprnbc',
'arnp',
'arnpbc',
'arnpc',
'bs',
'bsn',
'canp',
'ccns',
'ccrn',
'cfnp',
'cnm',
'cnnp',
'cnp',
'cns',
'crn',
'crna',
'crnp',
'cs',
'dcnp',
'dds',
'dmd',
'dnp',
'dpm',
'faafp',
'faca',
'facc',
'face',
'facg',
'facp',
'facs',
'fccp',
'fnp',
'fnpbc',
'fnpc',
'fpmhnp',
'fscai',
'fsvm',
'gnp',
'gnpbc',
'lacc',
'lp',
'ma',
'mb',
'mba',
'mbbch',
'mbbs',
'md',
'mhs',
'mms',
'mpas',
'mph',
'mrcp',
'ms',
'mshs',
'msn',
'naspe',
'nd',
'np',
'npp',
'od',
'pa',
'pac',
'pc',
'pharmd',
'phd',
'pmhnp',
'pmhnpbc',
'pmhnpc',
'psynp',
'pt',
'rn',
'rncs',
'rpac',
'rph',
'vmd',
'whnp',
]

# def comparing(cred):
#     for i in range(0, len(credentials)):
#         if credentials[i] == cred:
#             return(str(1))
#         else:
#             return(str(0))

# def gencredentials(credential):
#     sOutput = ""
#     for i in range(0, len(credentials)):
#         if str(credential) == str(credentials[i]):
#             sOutput += "'" + credentials[i] + "': 1,\n"
#         else:
#             sOutput += "'" + credentials[i] + "': 0,\n"
#     return sOutput

# print(gencredentials('phd'))

# def gencredentials(credential, gender, state, speciality, isopioidprescriber):
#     sOutput = ""
#     for i in range(0, len(credentials)):
#         if str(credential) == str(credentials[i]):
#             sOutput += "'" + credentials[i] + "': 1,\n"
#         else:
#             sOutput += "'" + credentials[i] + "': 0,\n"
#     sOutput += "gender: " + '<gender>\n'
#     sOutput += "state: " + '<state>\n'
#     sOutput += "speciality: " + '<speciality>\n'
#     sOutput += "isopioidprescriber: " + '<isopioidprescriber>\n'
#     return sOutput
# print(gencredentials('pt', 'male', 'AL', 'Nurse Practioner', 'yes'))

def comparethatstrin(strang, credential):
    if strang == credential:
        return("1")
    else:
        return("0")
credential = 'acnp'

# print(str(comparethatstrin('acnp',credential)))

