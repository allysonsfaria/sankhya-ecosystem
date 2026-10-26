---
id: "360053496574"
titulo: "Parâmetro TIPTABPRECOS - Quais as opções disponíveis para definição do controle das tabelas de preço "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360053496574-Par%C3%A2metro-TIPTABPRECOS-Quais-as-op%C3%A7%C3%B5es-dispon%C3%ADveis-para-defini%C3%A7%C3%A3o-do-controle-das-tabelas-de-pre%C3%A7o"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:28:39Z"
rotulos: ["#revisadohugo", "Produtos", "Configuração", "Parceiro", "Preferências", "Controle Flexível de Tabelas de Preço"]
---

# Parâmetro TIPTABPRECOS - Quais as opções disponíveis para definição do controle das tabelas de preço 

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19552318159127) SOLUÇÃO:**

A escolha de como serão controlados os preços dos produtos será registrada no parâmetro **"Tabela de preços por: - TIPTABPRECOS".**

- Tela 'Preferências' (Configurações » Avançado):

![Imagem 2: Tela 'Preferências' (Configurações » Avançado):](https://ajuda.sankhya.com.br/hc/article_attachments/360091460153)

Através desse parâmetro o usuário poderá escolher as seguintes opções:

**![Imagem 3: Única: Utiliza a tabela 0.](https://ajuda.sankhya.com.br/hc/article_attachments/20471803176727) Única:** Utiliza a tabela 0.

**![Imagem 4: Região do vendedor: Deve ser informada a tabela na tela 'Regiões' (Configurações » Cadastros » Endereços) , no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/19552318173463) Região do vendedor:** Deve ser informada a tabela na tela 'Regiões' (Configurações » Cadastros » Endereços), no campo 'Tabela Preço'. Além de definir a região do vendedor no campo região, do cadastro de vendedores.

**![Imagem 5: Região do Parceiro: Deve ser informada a tabela na tela 'Regiões' (Configurações » Cadastros » Endereços) , no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/19552318184599) Região do Parceiro:** Deve ser informada a tabela na tela 'Regiões' (Configurações » Cadastros » Endereços), no campo 'Tabela Preço'. Além de definir a região do parceiro no campo Região do cadastro de parceiros, aba endereços.

**![Imagem 6: Perfil: Informar a tabela de preços na tela 'Perfis' (Configurações » Cadastros) no campo 'Tabela de Preço'. Atenção:…](https://ajuda.sankhya.com.br/hc/article_attachments/19552274675863) Perfil:** Informar a tabela de preços na tela 'Perfis' (Configurações » Cadastros) no campo 'Tabela de Preço'. Atenção: no cadastro do parceiro, o perfil utilizado para obtenção da tabela de preços, será o configurado como: Perfil Principal.

**![Imagem 7: Parceiro: Informar a tabela de preços no cadastro de parceiros, aba Crédito no campo Tabela de preço.](https://ajuda.sankhya.com.br/hc/article_attachments/19552274682391) Parceiro:** Informar a tabela de preços no cadastro de parceiros, aba Crédito no campo Tabela de preço.

**![Imagem 8: Tipo de Negociação: Informar a tabela de preço no cadastro de 'Tipo de Negociação', aba características, no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/19552318224407) Tipo de Negociação:** Informar a tabela de preço no cadastro de 'Tipo de Negociação', aba características, no campo Tabela de Preço.

**![Imagem 9: Local: No cadastro de local informar a tabela de preço, no campo Tabela de Preço.](https://ajuda.sankhya.com.br/hc/article_attachments/19552318229911) Local:** No cadastro de local informar a tabela de preço, no campo Tabela de Preço.

**![Imagem 10: Tipo de Negociação/Vendedor : o sistema habilita a aba "Vendedor/Tabela" no cadastro de tipos de negociação, para que o…](https://ajuda.sankhya.com.br/hc/article_attachments/19552274701975) Tipo de Negociação/Vendedor**: o sistema habilita a aba "Vendedor/Tabela" no cadastro de tipos de negociação, para que o usuário ligue vendedores a diferentes tabelas de preços.

**![Imagem 11: Parceiro/Tipo Negociação/Vendedor - essa opção está disponível para MGE/W, o sistema olha primeiro no cadastro do…](https://ajuda.sankhya.com.br/hc/article_attachments/19552318248343) Parceiro/Tipo Negociação/Vendedor** - essa opção está disponível para MGE/W, o sistema olha primeiro no cadastro do parceiro a existência de uma tabela de preços e a utiliza, caso no parceiro não exista uma tabela de preços configurada o sistema utiliza a tabela de preços configurada no tipo de negociação para o vendedor da nota (aba Vendedor/Tabela do cadastro de tipo de negociação).

**![Imagem 12: Parceiro/Empresa: quando o parâmetro for configurado com esta opção, a tabela que for informada no campo 'Tabela de…](https://ajuda.sankhya.com.br/hc/article_attachments/19552318261911) Parceiro/Empresa:** quando o parâmetro for configurado com esta opção, a tabela que for informada no campo 'Tabela de Preço' da aba 'Grupo de ICMS/ISS por empresa [aba ativada pelo parâmetro EMPPRODIMPOST]', no cadastro do Parceiro, será a tabela que sugerirá o valor do produto nas movimentações de venda deste parceiro.

**Informações Importantes:**

- Se o parâmetro**"Usar Tabela de Preço da Empresa? - USARCODTABEMP"**estiver ligado e a tabela cadastrada na empresa for diferente de NULL, o sistema usará a tabela cadastrada na empresa.
- Na tela 'Regiões' o campo 'Tabela de Preço', poderá ser alterado para “Tab. Básica p/ Calc. de Acréscimo”, caso cliente trabalhe com o parâmetro **"Perc. retenção do acréscimo - PERCRETENCAO"** maior que zero.
