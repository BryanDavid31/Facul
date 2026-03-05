print('Qual é o seu ano de nascimento')
ano_nascimento = int(input())
idade = 2026 - ano_nascimento

print('Sua idade é,' ,idade, 'anos')

if idade < 18:
    print('Voce é menor de idade.')
    print('Voce precisa de uma autorização do responsavel')
    
else:
    print('voce e maior de idade.')
print('Tchau!')
