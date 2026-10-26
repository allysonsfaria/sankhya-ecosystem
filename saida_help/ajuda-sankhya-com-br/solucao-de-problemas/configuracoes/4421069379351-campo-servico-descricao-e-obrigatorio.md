---
id: "4421069379351"
titulo: "Campo \"serviço -> descrição\" é obrigatório"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4421069379351-Campo-servi%C3%A7o-descri%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3rio"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:19:30Z"
rotulos: ["Configuração", "Preferências", "#validadoLisiane", "Prefeituras", "NFS-e", "Problema de Campo Obrigatório na Descrição do Serviço", "Campo 'serviço -> descrição' é obrigatório", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS", "Documentos Eletrônicos"]
---

# Campo "serviço -> descrição" é obrigatório

Campo "servico -> descricao" é obrigatório

### SITUAÇÃO

Ao tentar emitir uma **"Nota Fiscal de Serviço Eletrônica (NFS-e)"**, o sistema apresenta a mensagem de erro informando que o campo **"servico -> descricao"** é obrigatório. A nota fica com status **"Aguardando Correção"** e, ao consultar o JSON da nota, identifica-se que o campo **"servico -> descricao"** está vazio ou não está sendo enviado corretamente, mesmo que haja informações de descrição do serviço.

### CAUSA

O erro ocorre quando o campo **"Conteúdo a ser enviado na descrição da NFS-e"** não está configurado nas preferências da empresa, ou está configurado de forma inadequada. Adicionalmente, pode ser causado por:

- Incompatibilidade na estrutura do **"JSON"** enviado à prefeitura quando o **"Código CNAE"** está preenchido no cadastro do produto/serviço e a nota contém múltiplos itens com valor.
- Ausência de informações configuradas nos campos de **"Tipo de Serviço"**.
- Outras causas: incompatibilidade entre o código de serviço municipal e as regras da prefeitura, uso de CEP inválido ou genérico.

### SOLUÇÃO

Para corrigir este erro, siga os passos abaixo:

**(1)** Acesse a tela **"Serviço"** (Configurações >> Cadastros >> Produtos >> Serviço), localize o serviço utilizado na nota e acesse a aba **"Impostos"**. Se necessário, remova o **"Código CNAE"** ou ajuste o campo **"Tipo de Serviço"**.

**(2)** Acesse a tela **"Empresa"** (Comercial>> Preferenciais) e localize a empresa emissora da nota.

**(3)** Clique na aba **"Documentos Eletrônicos"**.

**(4)** Acesse a aba**"NFS-e"** e localize o campo **"Conteúdo a ser enviado na descrição da NFS-e"**.

**(5)** Configure este campo com uma das opções disponíveis, como **"Descrição do Produto/Serviço"** ou **"Observações"**.

![Imagem 1: (5) Configure este campo com uma das opções disponíveis, como "Descrição do Produto/Serviço" ou "Observações" .](https://ajuda.sankhya.com.br/hc/article_attachments/41976007108119)

**(6)** Salve as alterações realizadas.

**(7)** Retorne à nota que apresentou o erro, duplique-a e exclua a nota anterior com erro (ou redigite os itens, conforme necessário).

**(8)** Confirme a nova nota e verifique se o erro foi corrigido.

**Dicas Adicionais:**

- **CEP:** Certifique-se de que o CEP informado é válido e reconhecido na base oficial dos Correios.
- **Configurações de Cidade:** Verifique as configurações específicas da cidade na tela **"Cidades"** (Configurações >> Cadastros >> Endereços >> Cidades), na aba **"NFS-e"**, especialmente os campos relacionados ao envio de quantidade, valor unitário e itens separados no JSON.
