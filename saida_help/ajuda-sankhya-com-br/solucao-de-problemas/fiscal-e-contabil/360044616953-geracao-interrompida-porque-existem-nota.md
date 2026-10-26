---
id: "360044616953"
titulo: "Geração interrompida porque existem notas nesse período com situação \"ENVIADA\", \"AGUARDANDO AUTORIZAÇÃO\" ou \"PENDENTE DE RETORNO\". Por exemplo, a nota com número único 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616953-Gera%C3%A7%C3%A3o-interrompida-porque-existem-notas-nesse-per%C3%ADodo-com-situa%C3%A7%C3%A3o-ENVIADA-AGUARDANDO-AUTORIZA%C3%87%C3%83O-ou-PENDENTE-DE-RETORNO-Por-exemplo-a-nota-com-n%C3%BAmero-%C3%BAnico-X"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-08-13T15:56:32Z"
rotulos: ["Configuração", "Relatórios", "NF-e", "SEFAZ", "LIV_E00243", "Notas com status \"ENVIADA\" \"AGUARDANDO AUTORIZAÇÃO\" \"PENDENTE DE RETORNO\"", "Localize a nota verifique \"Status NF-e\" e trate conforme status", "Geração interrompida por notas com status inválidos no período", "Erro", "Artigo atualizado KCS", "Fiscal/Contábil - KCS", "Documentos Eletrônicos"]
---

# Geração interrompida porque existem notas nesse período com situação "ENVIADA", "AGUARDANDO AUTORIZAÇÃO" ou "PENDENTE DE RETORNO". Por exemplo, a nota com número único 'X'

**MENSAGEM**

Geração interrompida porque existem notas nesse período com situação "ENVIADA", "AGUARDANDO AUTORIZAÇÃO" ou "PENDENTE DE RETORNO". Por exemplo, a nota com número único 'X'.

**SITUAÇÃO**

Esta mensagem aparece ao tentar realizar a geração do Livro ICMS/IPI ou a geração do ISS em um período que contém notas fiscais com situação indefinida. O sistema interrompe o processo e exibe um aviso informando que existem notas com status **"ENVIADA"**, **"AGUARDANDO AUTORIZAÇÃO"** ou **"PENDENTE DE RETORNO"**, impedindo a conclusão da geração dos livros fiscais.

**SOLUÇÃO**

A mensagem é um bloqueio do sistema, não apenas um aviso simples. Você não conseguirá gerar o livro fiscal enquanto houver notas com esses status, pois o sistema precisa que todas as notas do período estejam com situação definida (aprovadas, canceladas ou rejeitadas) para calcular corretamente os valores fiscais. Para resolver, siga os passos abaixo:

**(1)** Localize no Portal (Caminho de acesso: Compras » Vendas » Movimentação Interna) o número único citado na mensagem de erro;

**(2)** Selecione a nota, busque pelo campo **"Status NF-e";**

![Imagem 1: (2) Selecione a nota, busque pelo campo "Status NF-e";](https://ajuda.sankhya.com.br/hc/article_attachments/15238493250199)

**(3)** Caso não localize esse campo, o mesmo pode ser inserido através do botão **"Configuração da Grade":**

![Imagem 2: (3) Caso não localize esse campo, o mesmo pode ser inserido através do botão "Configuração da Grade":](https://ajuda.sankhya.com.br/hc/article_attachments/15238523062807)

Busque pelo campo **"Status NF-e"** em **"Colunas disponíveis"** e arraste para **"Colunas selecionadas"**.

**(4)** De acordo com o **"Status NF-e"** apresentado, proceda com as devidas tratativas:

- Aguardando Autorização: [Nota Fiscal Eletrônica com status 'Aguardando Autorização'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004833)
- Enviada: [Nota Fiscal Eletrônica com status 'Enviada'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044128313)
- Pendente de Retorno: [Nota Fiscal Eletrônica com status 'Pendente de Retorno'](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042507454)
- Se a nota apresenta erro na chave NF-e (modelo incorreto), exclua e relance a nota;
- Se a nota está travada e não permite ações, contate o suporte para análise de possíveis ajustes via banco de dados.

**(5)** Realizada a tratativa da respectiva nota, teste a geração dos livros novamente. Caso existam múltiplas notas, repita o processo para cada uma delas.

**CAUSA**

Ao realizar a geração de ICMS/IPI, se detectada a presença no período de notas fiscais com status NF-e 'Aguardando autorização', 'Pendente de retorno' ou 'Enviada', será apresentada a mensagem.
