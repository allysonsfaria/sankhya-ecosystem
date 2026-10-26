---
id: "360044605714"
titulo: "Configurações necessárias para habilitar a forma de pagamento da REDE"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605714-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-habilitar-a-forma-de-pagamento-da-REDE"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > E-commerce"
atualizado_em: "2026-07-29T14:37:05Z"
rotulos: ["Configuração", "Pagamentos", "Configurações necessárias para habilitar a forma de pagamento da REDE", "Painel Administrativo > MarketPlace > Web Service > Integrações", "Obter Access Token Número do PV", "Configurar valores parcelas habilitar forma de pagamento", "Rede", "Marketplace", "Integrações"]
---

# Configurações necessárias para habilitar a forma de pagamento da REDE

Para habilitar a REDE como forma de pagamento no site, é necessário a contratação dos serviço para que seja recebido o Acess Token e o Número do PV. Veja um exemplo:

**Acess Token:** fa27da4e88c21e84a764593684960c32

**API Key (PV):** 89152354

Para maiores informações acesse o [site da REDE.](https://www.userede.com.br/novo/e-rede)

**Configurações no Painel Administrativo:**

Acesse o Painel Administrativo da loja e, em seguida, clique na opção **"MarketPlace"**.

![Imagem 1: Acesse o Painel Administrativo da loja e, em seguida, clique na opção "MarketPlace" .](https://ajuda.sankhya.com.br/hc/article_attachments/360061012154)

Em seguida, clique no botão **"Acessar"** do Web Service**:**

![Imagem 2: Em seguida, clique no botão "Acessar" do Web Service :](https://ajuda.sankhya.com.br/hc/article_attachments/360061012174)

Dentro do Web Service,  na subseção **"Integrações"**, clique no botão **"Incluir"**:

![Imagem 3: Dentro do Web Service , na subseção "Integrações" , clique no botão "Incluir" :](https://ajuda.sankhya.com.br/hc/article_attachments/360061012194)

Configure conforme descrevemos abaixo:

- **Tipo de Integração:** REDECARD
- **Ambiente:** PRODUCTION
- **API URL:** https://api.userede.com.br/erede
- **API Key:**  89152354

**Observação:** Insira no API Key o número do PV repassado pela REDE.

- **ID Usuário:** não precisa
- **Senha:** não precisa
- **Access Token:** fa27da4e88c21e84a764593684960c32

**Observação:** Neste campo, insira também o Token repassado pela REDE.

![Imagem 4: Observação: Neste campo, insira também o Token repassado pela REDE .](https://ajuda.sankhya.com.br/hc/article_attachments/360061012214)

Ainda no Painel Administrativo, no botão **"Configurações"**, clique em Pagamentos no Varejo e/ou Atacado.

![Imagem 5: Ainda no Painel Administrativo , no botão "Configurações" , clique em Pagamentos no Varejo e/ou Atacado .](https://ajuda.sankhya.com.br/hc/article_attachments/360061934293)

Selecione a Forma de Pagamento da REDE:

![Imagem 6: Selecione a Forma de Pagamento da REDE :](https://ajuda.sankhya.com.br/hc/article_attachments/360061934313)

Realize as configurações conforme a necessidade das regras de negócio de sua empresa, com Valores mínimo e máximo, percentual de desconto, juros, quantidade de parcelas e afins.

### Imagem 7: Realize as configurações conforme a necessidade das regras de negócio de sua empresa, com Valores mínimo e máximo ,…

Por fim, marque para **"Habilitar"** a Forma de Pagamento.
