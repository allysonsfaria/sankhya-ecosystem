---
id: "360042867114"
titulo: "O valor '' do elemento 'descANP' não é válido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042867114-O-valor-do-elemento-descANP-n%C3%A3o-%C3%A9-v%C3%A1lido"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-21T12:59:57Z"
rotulos: ["#PUBLIFER", "Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "Corrigir campos na aba Combustível", "Erro na descrição ANP de produtos", "Ligar parâmetro de distribuidor de combustível", "Erro"]
---

# O valor '' do elemento 'descANP' não é válido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16453427104151) MENSAGEM:**

cvc-minLength-valid: O valor '' com tamanho = '0' não tem um aspecto válido em relação ao minLength '2' do tipo '#AnonType\_descANPcombproddetinfNFeTNFe'.
cvc-type.3.1.3: O valor '' do elemento 'descANP' não é válido.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453427107991) SITUAÇÃO:**

Ao realizar emissão de NF-e pela tela "**[Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)"** no **SankhyaW**, a nota ficará com Status: 'Aguardando Correção'. Acessando a opção (**...**)>>"**Ver Acompanhamento**", é possível consultar o detalhe da rejeição a seguir.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453442320407) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 4: Acesse a tela " Produtos " (Caminho de acesso à tela: Configurações » Cadastros » Produtos ).](https://ajuda.sankhya.com.br/hc/article_attachments/16453427116439) Acesse a tela "**[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)"** (Caminho de acesso à tela: Configurações » Cadastros » Produtos).

- Localize dentre os itens lançados na nota, aqueles com classificação de ST = Derivados de petróleo, lubrificantes e outros produtos. (Aba "**Impostos"**)
- Na aba "**Combustível"** de tais itens, certifique-se que os campos abaixo foram devidamente preenchidos:

![Imagem 5: Na aba " Combustível" de tais itens, certifique-se que os campos abaixo foram devidamente preenchidos:](https://ajuda.sankhya.com.br/hc/article_attachments/14396137299479)

![Imagem 6: Configurado os campos acima de forma adequada, redigite o cabeçalho da nota e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16453427121175) Configurado os campos acima de forma adequada, redigite o cabeçalho da nota e gere um novo lote.

**![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16453427124631) IMPORTANTE:**

Caso não visualize a aba combustível, ligue o parâmetro abaixo:
Tela 'Preferências' (Configurações » Avançado) >> Chave **COMBUSTIVEL** - Distribuidor de combustivel? = LIGADO

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16453427125783) CAUSA:**

Mensagem apresentada quando realizada emissão de NF-e com produtos Derivados de petróleo, lubrificantes e informado indevidamente informações de "Descrição ANP".
