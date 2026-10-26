---
id: "39267974157847"
titulo: "Por que aparecem eventos residuais 10180/10181 e 311 no cálculo da folha?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39267974157847-Por-que-aparecem-eventos-residuais-10180-10181-e-311-no-c%C3%A1lculo-da-folha"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:29Z"
rotulos: ["Configuração", "Eventos", "Cálculo", "Impostos", "Folha de Pagamento", "13º Salário", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Por que aparecem eventos residuais 10180/10181 e 311 no cálculo da folha?

Durante o cálculo da folha de pagamento, especialmente em dezembro, podem aparecer eventos residuais como **"10180"**, **"10181"** e **"311 - Desc Residuos Medias 13º"** que não eram esperados. Esses eventos são gerados automaticamente pelo sistema como parte do processo de reprocessamento das médias do 13º salário.

O sistema realiza um recálculo das médias utilizando os valores apurados no mês de dezembro, comparando-os com os valores já pagos anteriormente. Esse processo pode resultar na geração de eventos de ajuste, tanto para desconto quanto para pagamento.

### Como funciona o reprocessamento das médias

No cálculo da referência de dezembro, o sistema executa automaticamente o reprocessamento das médias do 13º salário, utilizando as médias apuradas neste mês. A partir desse recálculo, as médias do 13º salário são ajustadas, podendo ocorrer duas situações:

**Geração de residuais para desconto:** quando o 13º salário foi pago a maior, o sistema gera eventos de desconto e pode incluir o ressarcimento de INSS e IRRF através dos eventos **"925 - Restituição INSS 13º"** e **"926 - Restituição IRRF 13º"**.

**Geração de residuais para pagamento:** quando o 13º salário foi pago a menor, considerando que o colaborador possuía médias superiores às inicialmente apuradas, o sistema gera eventos de pagamento complementar.

### Entendendo o evento 311

O evento **"311 - Desc Residuos Medias 13º"** representa a diferença entre as médias calculadas na 2ª parcela do 13º salário e as médias recalculadas na folha mensal de dezembro. Este evento é calculado da seguinte forma:

O sistema soma todos os eventos que compõem as médias na aba de médias da folha do 13º salário, divide por 12 e multiplica pelo número de meses trabalhados. Em seguida, realiza o mesmo cálculo com os valores da folha mensal de dezembro. A diferença entre esses dois valores resulta no evento 311.

Este evento impacta diretamente as bases de **INSS** e **IRRF**, gerando os respectivos eventos de ressarcimento quando aplicável.

### Eventos 10180 e 10181

Os eventos **"10180"** e **"10181"** são eventos residuais relacionados a ajustes de médias ou outros cálculos específicos do 13º salário. Quando aparecem indevidamente na folha mensal, geralmente indicam que:

• Há um lançamento manual anterior que não foi excluído da tela **"Movimentos"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento)
• O evento está configurado para ser recalculado em folhas específicas
• Existe alguma configuração no cadastro do colaborador que está gerando o evento automaticamente

### Como verificar e corrigir eventos indevidos

Para verificar se os eventos residuais são devidos ou indevidos, siga os passos abaixo:

**(1)** Acesse a tela **"Lançamento de Movimentos"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento) e verifique se há lançamentos manuais dos eventos 10180 ou 10181 que não deveriam estar presentes.

**(2)** Caso identifique lançamentos indevidos, exclua-os manualmente da tela de movimentos.

**(3)** Recalcule a folha de pagamento para verificar se os eventos ainda aparecem.

**(4)** Se o 311 aparecer, verifique na aba de **"Médias"** da folha do 13º e da folha mensal se há diferença nos valores que justifique o ajuste.

Caso os eventos residuais sejam legítimos e representem ajustes reais nas médias do 13º salário, eles devem ser mantidos no cálculo, pois garantem a conformidade dos valores pagos com os direitos do colaborador.
