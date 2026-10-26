---
id: "44011095800343"
titulo: "Como integrar o Omie ERP com o Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011095800343-Como-integrar-o-Omie-ERP-com-o-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:55:38Z"
rotulos: ["sync_hc", "magis5", "magis5_204055258242", "sync_hash_9d427882319b"]
---

# Como integrar o Omie ERP com o Magis5 Hub?

## Veja como realizar integração da sua conta Magis5 Hub com o seu Omie ERP

---

O Omie ERP é um sistema simples e intuitivo de gestão empresarial que auxilia em segmentos como Vendas e NF, Finanças, Estoque e Produção, Serviços, etc. Você pode integrá-lo com o Magis5 Hub para gerenciar seus canais de vendas online.

### 1) Obtendo a APP KEY dentro do Omie

💡  Apenas os da conta Omie conseguem obter a chave de integração

**Acesse o painel do Omie ERP.** A partir disto, serão exibidos todos os aplicativos que o seu cadastro tem acesso.

Após isso clique em **"Mais opções" (ícone de engrenagem![engrenagemAz](https://ajuda.sankhya.com.br/hc/article_attachments/44011074603671))**, conforme indicado na imagem abaixo:

![Imagem 2: Após isso clique em "Mais opções" (ícone de engrenagem ) , conforme indicado na imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44011107377047)

Rolando a página até o final, você irá encontrar a área com a Chave de Integração. Copie e guarde os códigos dos campos **APP\_KEY** e **APP\_SECRET**:![AppKeyAppSecret](https://ajuda.sankhya.com.br/hc/article_attachments/44011107517207)

Uma dica é abrir um **Bloco de Notas**no seu computador e separar os dados necessários para a integração. Assim, fica mas fácil pra você se guiar durante o processo!

Após ter copiado os códigos, prossiga para sua conta Magis5.

### 2) Integrando o Omie ERP com o Magis5 Hub

No Magis5 Hub, vá até **"Configurações" > "Integrações"**e depois clique em **"ERPs & Faturador".**

![Imagem 4: No Magis5 Hub, vá até "Configurações" > "Integrações" e depois clique em "ERPs & Faturador".](https://ajuda.sankhya.com.br/hc/article_attachments/44011074961431)

Após isso, clique em**“Novo”.**

![Imagem 5: Após isso, clique em “Novo”.](https://ajuda.sankhya.com.br/hc/article_attachments/44011107749015)

No formulário de nova integração que for aberto, selecione **Omie** nas opções de ERP e preencha os campos conforme demonstrado:

![Imagem 6: No formulário de nova integração que for aberto, selecione Omie nas opções de ERP e preencha os campos conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/44011096506903)

**Descrição:**Digite o nome da empresa cadastrada em seu Omie ERP;
**Usuário:**O usuário copiado no item **[APP\_KEY](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011095800343-Como-integrar-o-Omie-ERP-com-o-Magis5-Hub#app)** do Omie ERP;
**Senha:** A senha copiada na **[APP\_SECRET](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011095800343-Como-integrar-o-Omie-ERP-com-o-Magis5-Hub#app)** do Omie ERP;
**ERP principal:** Ative esta flag **apenas** se for o primeiro ERP que está integrando;
**Quantidade de item por Volume:** Quantidade de itens que vão dentro da caixa no pedido. Campo vinculado ao **pedido**, e não ao item.

💡 **O que é o ERP Principal?**

Ele é que será responsável por controlar o estoque de seus produtos e normalmente é o primeiro a ser integrado.

Caso você tenha mais de uma filial para emissão de Notas Fiscais você também poderá definir **ERPs Secundários** usando a funcionalidade de [Múltiplos ERPs](https://ajuda.magis5.com.br/faq/configuracao-de-multiplos-cnpjs-de-faturamento?hsLang=pt-br).

A funcionalidade de Múltiplos ERPs pode ser utilizada quando você possui mais de um CNPJ e precisa emitir Notas Fiscais nas diferentes empresas

Na aba **Depósitos**insira o código do depósito que será utilizado para gerenciar o estoque de seus produtos. Para obter esse código, você terá que [solicitá-lo com o suporte do Omie](https://www.omie.com.br/suporte/). **Caso não preencha com esse código, o Magis5 Hub irá utilizar o depósito do Omie que estiver definido como padrão.**

![Imagem 7: A funcionalidade de Múltiplos ERPs pode ser utilizada quando você possui mais de um CNPJ e precisa emitir Notas Fiscais…](https://ajuda.sankhya.com.br/hc/article_attachments/44011107935895)

Não é necessário preencher os campos na aba Dados adicionais.

Feitos todos os procedimentos acima, finalize a integração clicando no botão **Salvar**.

![Imagem 8: A funcionalidade de Múltiplos ERPs pode ser utilizada quando você possui mais de um CNPJ e precisa emitir Notas Fiscais…](https://ajuda.sankhya.com.br/hc/article_attachments/44011142589591)

Caso tenha dúvidas, [entre em contato com nosso suporte](https://ajuda.magis5.com.br/como-abrir-um-suporte-por-bate-papo-na-magis5?hsLang=pt-br).

**⚠️ Observações para cadastro de produtos no Omie ERP através do Magis5 Hub:**

**- Obrigatório o cadastro de NCM no produto;
- Não é possível cadastrar SKUs diferentes que tenham o mesmo EAN.**
