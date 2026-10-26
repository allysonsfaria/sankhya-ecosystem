---
id: "360042623854"
titulo: "The value '' of element 'descANP' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042623854-The-value-of-element-descANP-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:52Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "Combustível", "Cadastro de Produtos", "Valor Inválido de 'descANP'", "Erro"]
---

# The value '' of element 'descANP' is not valid

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16443885437847) **MENSAGEM:**

cvc-minLength-valid: Value '' with length = '0' is not facet-valid with respect to minLength '2' for type '#AnonType\_descANPcombproddetinfNFeTNFe'. cvc-type.3.1.3: The value '' of element '**descANP**' is not valid.

**![Imagem 2: SOLUÇÃO: Para correção deste erro, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16443885440663) SOLUÇÃO:**
Para correção deste erro, siga os passos abaixo:

![Imagem 3: Acesse a tela Preferências (Caminho de acesso à tela: Configurações » Avançado)](https://ajuda.sankhya.com.br/hc/article_attachments/16443885441943) Acesse a tela Preferências (Caminho de acesso à tela: Configurações » Avançado)

**(2)** Habilite o parâmetro '**COMBUSTIVEL' - Distribuidor de combustível?**

![Imagem 4: Vá até a tela de " Cadastro de Produtos ":](https://ajuda.sankhya.com.br/hc/article_attachments/16443885447575) Vá até a tela de "**[Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)":**

**(2)** Selecione o produto a ser ajustado, e na aba **"Combustível"** preencha os campos abaixo conforme necessidade para o respectivo item:

(3)**"Descrição ANP"**

(3)**"Valor de Partida GLP (sem ICMS)"**

**(2)**Para os demais campos citados abaixo, atente-se ao fato de que a soma dos três deve totalizar 0 ou 100 :

(3)**"Percentual de mistura GLP";**

(3)**"Percentual de mistura de Gás natural nacional";**

(3)**"Percentual de mistura de Gás natural importado".**

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16443910162455) IMPORTANTE:**

Os dados acima **não** são de responsabilidade do Service Desk, são informações relacionadas ao produto e de responsabilidade do cliente.

Essa validação será apenas um alerta, ou seja, o sistema permitirá que o usuário salve esse registro.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16443910162967) CAUSA:**

Na emissão de uma NF-e na versão 4.0, caso a nota possua produtos Combustíveis e o produto estiver com o cadastro incompleto na aba: Combustível, ocorrerá a Rejeição.

![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17855535924247) **OBSERVAÇÃO:**

([NT2016/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=qsg%20ostnbKY=)) - Nota Técnica.
