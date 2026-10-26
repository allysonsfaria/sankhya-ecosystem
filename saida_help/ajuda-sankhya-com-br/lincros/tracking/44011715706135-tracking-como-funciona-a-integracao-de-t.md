---
id: "44011715706135"
titulo: "[Tracking] Como funciona a integração de temperatura no Lincros Tracking?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011715706135--Tracking-Como-funciona-a-integra%C3%A7%C3%A3o-de-temperatura-no-Lincros-Tracking"
trilha: "Lincros > Tracking"
atualizado_em: "2026-10-05T19:09:36Z"
rotulos: ["sync_hc", "lincros", "sync_hash_eed91ff933d2", "lincros_13434769"]
---

# [Tracking] Como funciona a integração de temperatura no Lincros Tracking?

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44011722708503)

O cálculo da eficiência da temperatura define se uma viagem será aprovada ou reprovada, com base no tempo que o veículo envia informações de temperatura dentro do range predeterminado. Entender o método de cálculo da eficiência ajudará você a entender as premissas que serão apresentadas em seguida.

## Cálculo da eficiência

Para entender melhor, observe a imagem abaixo indicando as colunas utilizadas para o calculo da eficiência de temperatura.

![Imagem 2: Para entender melhor, observe a imagem abaixo indicando as colunas utilizadas para o calculo da eficiência de…](https://ajuda.sankhya.com.br/hc/article_attachments/44011730973975)

**Cálculo**: 02:30:28 / 04:15:13 = 0,5895

1. **Tempo Atual da Rota**: Tempo total da rota até o momento da consulta. O tempo é contabilizado desde o início da viagem até a conclusão de todas as entregas da viagem, ou o fim da rota (para viagens com devoluções aceitas).
2. **Tempo Dentro da Faixa**: Tempo total que a temperatura ficou dentro da faixa estabelecida.
3. **%Eficiência**: O indicador é resultado da divisão do tempo dentro da faixa pelo tempo atual da rota. A operação aritmética é: Eficiência = Tempo Atual da Rota / Tempo Dentro da Faixa

Se em uma viagem houver produtos de dois tipos, com duas metas diferentes, a meta válida é a meta do produto mais frio, isto é, o tipo de produto com a menor “**Temperatura mínima**” do “**Tipo de Produto**”.

## Premissas de funcionamento

Antes de verificarmos como funciona e quais são as configurações necessárias, é preciso verificar se a tecnologia é homologada pela Lincros. Hoje possuímos as seguintes integrações de temperatura para o Tracking.

- Sascar
- Onixsat
- Omnilink
- Quantenus
- PackId
- Positron
- Ravex

Agora que sabemos quais são as tecnologias homologadas para que seja captado a temperatura, vamos entender quais são as premissas para que a temperatura seja integrada.

## Cadastro do “Tipo do Produto”

O **Tipo de Produto** é definido no envio/importação da viagem, porém não é vinculado o range de temperatura automaticamente. Portanto, é recomendado que os tipos de produto sejam criados previamente, durante o processo de implantação.

Para criar ou alterar as metas de temperatura por **Tipo de Produto**, acesse o “Cadastros” → “Tipo de Produto”, edite ou crie o tipo e informe qual é a temperatura máxima e mínima do range.

![Imagem 3: Para criar ou alterar as metas de temperatura por Tipo de Produto , acesse o “Cadastros” → “Tipo de Produto”, edite ou…](https://ajuda.sankhya.com.br/hc/article_attachments/44011722970007)

## Cadastro do “Tipo de Veículo”

O **Tipo do Veículo** define o percentual de aprovação de eficiência de uma determinada viagem. Dependendo do tipo do veículo, a meta de eficiência pode variar.

![Imagem 4: O Tipo do Veículo define o percentual de aprovação de eficiência de uma determinada viagem. Dependendo do tipo do…](https://ajuda.sankhya.com.br/hc/article_attachments/44011703167511)

Nesse caso abaixo, podemos verificar, que com a meta em 70%, o índice de aprovação está **verde**, ou seja, acima da meta. Caso tivesse abaixo, estaria com o indicador **vermelho**.

![Imagem 5: Nesse caso abaixo, podemos verificar, que com a meta em 70%, o índice de aprovação está verde , ou seja, acima da meta.…](https://ajuda.sankhya.com.br/hc/article_attachments/44011716405143)

Para visualizar o gráfico de temperatura, clique sobre o ícone do termômetro presente na grid “**Entregas**”. É possível visualizar o “**Histórico de temperatura**” e quais temperaturas são registrados dentro e fora da faixa permitida.

![Imagem 6: Para visualizar o gráfico de temperatura, clique sobre o ícone do termômetro presente na grid “ Entregas ”. É possível…](https://ajuda.sankhya.com.br/hc/article_attachments/44011723415575)

## Recapitulando

- O “**Tempo Atual da Rota**” para de ser contabilizado após o apontamento de todas as entregas. Caso haja pelo menos uma entrega com o status **devolvido**, **revertido** ou **reentrega**. O tempo só para de ser contabilizado no momento que a rota é finalizada ou quando todas entregas são marcadas como **entregue**.
- A faixa de temperatura pode variar na mesma rota, ou seja, se houve 2 tipos de produtos, cuja o range seja diferente, durante a rota pode ser alterado à medida que as entregas são confirmadas.
