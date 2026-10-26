---
id: "11481456834071"
titulo: "Erro ao cancelar NFS-e. Código do município do prestador inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/11481456834071-Erro-ao-cancelar-NFS-e-C%C3%B3digo-do-munic%C3%ADpio-do-prestador-inv%C3%A1lido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:01:39Z"
rotulos: ["Configuração", "Parceiro", "Cidades", "não apagar", "BTH17", "Prefeituras", "NFS-e", "Correção de Código Municipal em NFS-e", "Erro"]
---

# Erro ao cancelar NFS-e. Código do município do prestador inválido

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16305161306135) MENSAGEM**:

[BTH17]: Código do município do prestador inválido. Possível solução: Informe o código do município do prestador do serviço, conforme Tabela de Municípios do IBGE."

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16305161310999) SOLUÇÃO:**

- Verifique a nota em questão, na tabela TGFCAB, se o campo **"CODCID"** (Código Cidade) está preenchido (campo do cabeçalho da nota);
- Caso este campo não esteja preenchido, o sistema irá verificar o endereço/código do município cadastrado na tela de Parceiro.;
- Acesse a tela **"[Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)"** e inclua o campo **"Cidade"** no layout;
- Informe o código da cidade na nota;
- Realize o cancelamento da NFS-e.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16305161313175) CAUSA:**

Este erro ocorre quando o código do município é diferente do código do município da prefeitura que irá realizar o cancelamento.

- Exemplo: Prefeitura de Lages - SC e parceiro de Uberlândia - MG, caso o campo CODCID não esteja preenchido no cabeçalho da nota, o sistema irá verificar o cadastro do parceiro (Uberlândia - MG) e levar o código do município de Uberlândia. Desta forma, quando o sistema tentar realizar o cancelamento juntamente com a prefeitura o código irá ser divergente, assim apresentando o erro, visto que não é o código de Lages- SC.
- Exemplo: Com o campo CODCID preenchido no cabeçalho da nota, o sistema irá olhar diretamente para a cidade informada, assim, trazendo o código correto do município para realizar o cancelamento.

Identificando este erro no log do sistema Sankhya

- Ative o parâmetro "**Imprimir os XMLs processados pelo SanNFe no log?-DEBUGXML"**, realize o teste de cancelamento;
- Faça o download do server.log;
- No log com o parâmetro "**Imprimir os XMLs processados pelo SanNFe no log?-DEBUGXML"** ativado, será apresentado o erro conforme exemplo:

![Imagem 4: No log com o parâmetro " Imprimir os XMLs processados pelo SanNFe no log?-DEBUGXML" ativado, será apresentado o erro…](https://ajuda.sankhya.com.br/hc/article_attachments/14628656295319)
