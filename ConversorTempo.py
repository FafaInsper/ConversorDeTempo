print('SEJA BEM-VINDO AO CONVERSOR DE TEMPO! Feito por Fafa')

# Inserir a quantidade e o tipo de tempo
condinicial = input("Qual a medida de tempo que você quer converter? (Segundos, Minutos, Horas, Dias, Semanas, Meses, Anos, Décadas ou Séculos) ")
numinicial = float(input("Digite o número para a condição que você definiu antes: "))

# Inserir a medida que ele quer traduzir
condfinal = input('Para qual medida de tempo você quer converter? (Segundos, Minutos, Horas, Dias, Semanas, Meses, Anos, Décadas ou Séculos) ')


if condinicial == 'Segundos' or condinicial == 'segundos':
    if condfinal == 'Segundos' or condfinal == 'segundos':
        numfinal = numinicial
    if condfinal == 'Minutos' or condfinal == 'minutos':
        numfinal = numinicial / 60
    if condfinal == 'Horas' or condfinal == 'horas':
        numfinal = numinicial / 3600
    if condfinal == 'Dias' or condfinal == 'dias':
        numfinal = numinicial / 86400
    if condfinal == 'Semanas' or condfinal == 'semanas':
        numfinal = numinicial / 604800
    if condfinal == 'Meses' or condfinal == 'meses':
        numfinal = numinicial / 2592000
    if condfinal == 'Anos' or condfinal == 'anos':
        numfinal = numinicial / 31104000
    if condfinal == 'Décadas' or condfinal == 'décadas' or condfinal == 'Decadas' or condfinal == 'decadas':
        numfinal = numinicial / 311040000
    if condfinal == 'Séculos' or condfinal == 'séculos' or condfinal == 'Seculos' or condfinal == 'seculos':
        numfinal = numinicial / 3110400000
    else:
        print('Medida de tempo não encontrada! Tente novamente!')
elif condinicial == 'Minutos' or condinicial == 'minutos':
    if condfinal == 'Segundos' or condfinal == 'segundos':
        numfinal = numinicial * 60
    if condfinal == 'Minutos' or condfinal == 'minutos':
        numfinal = numinicial 
    if condfinal == 'Horas' or condfinal == 'horas':
        numfinal = numinicial / 60
    if condfinal == 'Dias' or condfinal == 'dias':
        numfinal = numinicial / 1440
    if condfinal == 'Semanas' or condfinal == 'semanas':
        numfinal = numinicial / 10080
    if condfinal == 'Meses' or condfinal == 'meses':
        numfinal = numinicial / 43200
    if condfinal == 'Anos' or condfinal == 'anos':
        numfinal = numinicial / 518400
    if condfinal == 'Décadas' or condfinal == 'décadas' or condfinal == 'Decadas' or condfinal == 'decadas':
        numfinal = numinicial / 5184000
    if condfinal == 'Séculos' or condfinal == 'séculos' or condfinal == 'Seculos' or condfinal == 'seculos':
        numfinal = numinicial / 51840000
    else:
        print('Medida de tempo não encontrada! Tente novamente!')
elif condinicial == 'Horas' or condinicial == 'horas':
    if condfinal == 'Segundos' or condfinal == 'segundos':
        numfinal = numinicial * 3600
    if condfinal == 'Minutos' or condfinal == 'minutos':
        numfinal = numinicial * 60
    if condfinal == 'Horas' or condfinal == 'horas':
        numfinal = numinicial 
    if condfinal == 'Dias' or condfinal == 'dias':
        numfinal = numinicial / 24
    if condfinal == 'Semanas' or condfinal == 'semanas':
        numfinal = numinicial / 168
    if condfinal == 'Meses' or condfinal == 'meses':
        numfinal = numinicial / 720
    if condfinal == 'Anos' or condfinal == 'anos':
        numfinal = numinicial / 8640
    if condfinal == 'Décadas' or condfinal == 'décadas' or condfinal == 'Decadas' or condfinal == 'decadas':
        numfinal = numinicial / 86400
    if condfinal == 'Séculos' or condfinal == 'séculos' or condfinal == 'Seculos' or condfinal == 'seculos':
        numfinal = numinicial / 864000
    else:
        print('Medida de tempo não encontrada! Tente novamente!')
elif condinicial == 'Dias' or condinicial == 'dias':
    if condfinal == 'Segundos' or condfinal == 'segundos':
        numfinal = numinicial * 86400
    if condfinal == 'Minutos' or condfinal == 'minutos':
        numfinal = numinicial * 1440
    if condfinal == 'Horas' or condfinal == 'horas':
        numfinal = numinicial * 24
    if condfinal == 'Dias' or condfinal == 'dias':
        numfinal = numinicial
    if condfinal == 'Semanas' or condfinal == 'semanas':
        numfinal = numinicial / 7
    if condfinal == 'Meses' or condfinal == 'meses':
        numfinal = numinicial / 30
    if condfinal == 'Anos' or condfinal == 'anos':
        numfinal = numinicial / 365
    if condfinal == 'Décadas' or condfinal == 'décadas' or condfinal == 'Decadas' or condfinal == 'decadas':
        numfinal = numinicial / 3650
    if condfinal == 'Séculos' or condfinal == 'séculos' or condfinal == 'Seculos' or condfinal == 'seculos':
        numfinal = numinicial / 36500
    else:
        print('Medida de tempo não encontrada! Tente novamente!')
elif condinicial == 'Semanas' or condinicial == 'semanas':
    if condfinal == 'Segundos' or condfinal == 'segundos':
        numfinal = numinicial * 604800
    if condfinal == 'Minutos' or condfinal == 'minutos':
        numfinal = numinicial * 10080
    if condfinal == 'Horas' or condfinal == 'horas':
        numfinal = numinicial * 168
    if condfinal == 'Dias' or condfinal == 'dias':
        numfinal = numinicial * 7 
    if condfinal == 'Semanas' or condfinal == 'semanas':
        numfinal = numinicial
    if condfinal == 'Meses' or condfinal == 'meses':
        numfinal = numinicial / 4
    if condfinal == 'Anos' or condfinal == 'anos':
        numfinal = numinicial / 48
    if condfinal == 'Décadas' or condfinal == 'décadas' or condfinal == 'Decadas' or condfinal == 'decadas':
        numfinal = numinicial / 480
    if condfinal == 'Séculos' or condfinal == 'séculos' or condfinal == 'Seculos' or condfinal == 'seculos':
        numfinal = numinicial / 4800
    else:
        print('Medida de tempo não encontrada! Tente novamente!')
elif condinicial == 'Meses' or condinicial == 'meses':
    if condfinal == 'Segundos' or condfinal == 'segundos':
        numfinal = numinicial * 2592000
    if condfinal == 'Minutos' or condfinal == 'minutos':
        numfinal = numinicial * 43200
    if condfinal == 'Horas' or condfinal == 'horas':
        numfinal = numinicial * 720
    if condfinal == 'Dias' or condfinal == 'dias':
        numfinal = numinicial * 30
    if condfinal == 'Semanas' or condfinal == 'semanas':
        numfinal = numinicial * 4
    if condfinal == 'Meses' or condfinal == 'meses':
        numfinal = numinicial
    if condfinal == 'Anos' or condfinal == 'anos':
        numfinal = numinicial / 12
    if condfinal == 'Décadas' or condfinal == 'décadas' or condfinal == 'Decadas' or condfinal == 'decadas':
        numfinal = numinicial / 120
    if condfinal == 'Séculos' or condfinal == 'séculos' or condfinal == 'Seculos' or condfinal == 'seculos':
        numfinal = numinicial / 1200
    else:
        print('Medida de tempo não encontrada! Tente novamente!')
elif condinicial == 'Anos' or condinicial == 'anos':
    if condfinal == 'Segundos' or condfinal == 'segundos':
        numfinal = numinicial * 31536000
    if condfinal == 'Minutos' or condfinal == 'minutos':
        numfinal = numinicial * 525600
    if condfinal == 'Horas' or condfinal == 'horas':
        numfinal = numinicial * 8760
    if condfinal == 'Dias' or condfinal == 'dias':
        numfinal = numinicial * 365
    if condfinal == 'Semanas' or condfinal == 'semanas':
        numfinal = numinicial * 48
    if condfinal == 'Meses' or condfinal == 'meses':
        numfinal = numinicial * 12
    if condfinal == 'Anos' or condfinal == 'anos':
        numfinal = numinicial
    if condfinal == 'Décadas' or condfinal == 'décadas' or condfinal == 'Decadas' or condfinal == 'decadas':
        numfinal = numinicial / 10
    if condfinal == 'Séculos' or condfinal == 'séculos' or condfinal == 'Seculos' or condfinal == 'seculos':
        numfinal = numinicial / 100
    else:
        print('Medida de tempo não encontrada! Tente novamente!')
elif condinicial == 'Décadas' or condinicial == 'décadas' or condinicial == 'Decadas' or condinicial == 'decadas':
    if condfinal == 'Segundos' or condfinal == 'segundos':
        numfinal = numinicial * 315360000
    if condfinal == 'Minutos' or condfinal == 'minutos':
        numfinal = numinicial * 5256000
    if condfinal == 'Horas' or condfinal == 'horas':
        numfinal = numinicial * 87600
    if condfinal == 'Dias' or condfinal == 'dias':
        numfinal = numinicial * 3650
    if condfinal == 'Semanas' or condfinal == 'semanas':
        numfinal = numinicial * 480
    if condfinal == 'Meses' or condfinal == 'meses':
        numfinal = numinicial * 120 
    if condfinal == 'Anos' or condfinal == 'anos':
        numfinal = numinicial * 10
    if condfinal == 'Décadas' or condfinal == 'décadas' or condfinal == 'Decadas' or condfinal == 'decadas':
        numfinal = numinicial
    if condfinal == 'Séculos' or condfinal == 'séculos' or condfinal == 'Seculos' or condfinal == 'seculos':
        numfinal = numinicial / 10
    else:
        print('Medida de tempo não encontrada! Tente novamente!')
elif condinicial == 'Séculos' or condinicial == 'séculos' or condinicial == 'Seculos' or condinicial == 'seculos':
    if condfinal == 'Segundos' or condfinal == 'segundos':
        numfinal = numinicial * 3153600000
    if condfinal == 'Minutos' or condfinal == 'minutos':
        numfinal = numinicial * 52560000
    if condfinal == 'Horas' or condfinal == 'horas':
        numfinal = numinicial * 876000
    if condfinal == 'Dias' or condfinal == 'dias':
        numfinal = numinicial * 36500
    if condfinal == 'Semanas' or condfinal == 'semanas':
        numfinal = numinicial * 4800
    if condfinal == 'Meses' or condfinal == 'meses':
        numfinal = numinicial * 1200
    if condfinal == 'Anos' or condfinal == 'anos':
        numfinal = numinicial * 100
    if condfinal == 'Décadas' or condfinal == 'décadas' or condfinal == 'Decadas' or condfinal == 'decadas':
        numfinal = numinicial * 10
    if condfinal == 'Séculos' or condfinal == 'séculos' or condfinal == 'Seculos' or condfinal == 'seculos':
        numfinal = numinicial 
    else:
        print('Medida de tempo não encontrada! Tente novamente!')


print('{} {} ficariam {} {}!'.format(numinicial, condinicial, numfinal, condfinal))

print('Obrigado para usar o Conversor do Fafa! Esperamos ter ajudado!')
