---
id: "8425445556119"
titulo: "As notas geradas no Sankhya, estão sendo validadas na prefeitura com data retroativa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8425445556119-As-notas-geradas-no-Sankhya-est%C3%A3o-sendo-validadas-na-prefeitura-com-data-retroativa"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:11:58Z"
rotulos: ["Configuração", "Preferências", "não apagar", "Prefeituras", "NFS-e", "Validação retroativa", "Habilite parâmetro", "Envio via webservice"]
---

# As notas geradas no Sankhya, estão sendo validadas na prefeitura com data retroativa

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16595805365783) MENSAGEM**:

As notas geradas no sankhya, estão sendo validadas na prefeitura com data retroativa.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16595777918999) SOLUÇÃO:**

Acesse o parâmetro **"CONDTCOMPFUSZER",** na tela **"Preferências"** (Caminho de acesso à tela: Configurações » Avançado » Preferências) e habilite-o. Quando esse parâmetro está ligado, se houver alguma NFS-e enviada via API, na geração do JSON, a competência da NFS-e não irá retroceder para o dia anterior caso seja emitida nas primeiras horas do dia.

![Imagem 3: Acesse o parâmetro " CONDTCOMPFUSZER", na tela "Preferências" (Caminho de acesso à tela: Configurações » Avançado »…](https://ajuda.sankhya.com.br/hc/article_attachments/9214345545495)

**Exemplo:**

A data competência foi de fato enviada no dia 01/08/2022, porém, às 0h. Trabalhamos com o UCT -3 ou seja, -3horas, então essa requisição foi enviada com a competência retroativa para 21h do dia 31/07/2022. 

![Imagem 4: A data competência foi de fato enviada no dia 01/08/2022, porém, às 0h. Trabalhamos com o UCT -3 ou seja, -3horas,…](https://ajuda.sankhya.com.br/attachments/token/FOoFdcniOA3OWhIVqPW6PubND/?name=image.png)

**Referente ao UTC:**

O formato de envio da data de competência das notas segue o UTC (Tempo Universal Coordenado), que é utilizado para padronizar os horários mundiais.

No Brasil existem quatro tipos de horários e o padrão é o horário de Brasília que é "**UTC -3**". Neste caso, ao informar a data de competência é preciso considerar que o horário de Brasília equivalerá a -3 horas do horário que você informou no campo.

Assim como se deve considerar em Brasília, é preciso considerar a mesma situação para os demais estados do Brasil que tem fuso horário diferente.

**Fusos do Brasil**:

**(1)** UTC -2: Horário Padrão de Fernando de Noronha - Esse fuso compreende as ilhas de Fernando de Noronha, Trindade, Martim Vaz e Penedos de São Pedro e São Paulo.

**(1)** UTC -3: Horário Padrão de Brasília - Esse fuso compreende a maior parte do território brasileiro incluindo a Capital Federal, Brasília. Fazem parte desse fuso da região Nordeste, região Sudeste, região Sul e partes das regiões Norte e Centro-Oeste.

**(1)** UTC -4: Horário Padrão do Amazonas - Esse fuso tem uma hora a menos em comparação com a Capital Federal. Ele compreende o Estado do Mato Grosso, o Estado do Mato Grosso do Sul, o Estado de Roraima, Rondônia e grande parte do estado do Amazonas.

**(1)** UTC -5: Horário Padrão do Acre - Esse fuso compreende o estado do Acre e o sudoeste do Amazonas.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16595777921687)CAUSA:**

Quando é feito o envio de um horário para a prefeitura via webservice.
