---
id: "35268455891991"
titulo: "Ajuste de Saldo de Rastreamento de Estoque ST"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35268455891991-Ajuste-de-Saldo-de-Rastreamento-de-Estoque-ST"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:25:43Z"
rotulos: ["Configuração", "TOP", "Estoque", "Preferências", "Ajuste de Saldo de Rastreamento de Estoque ST", "Saldo de Rastreamento de Estoque ST", "divergência entre o estoque próprio e o saldo de rastreamento (ST", "saldo de rastreamento apresenta quantidade inferior", "Ajuste"]
---

# Ajuste de Saldo de Rastreamento de Estoque ST

Em determinadas situações, pode ocorrer divergência entre o **estoque próprio** e o **saldo de rastreamento (ST)** de um item.
Um exemplo comum é quando o estoque próprio está correto, mas o saldo de rastreamento apresenta quantidade inferior.

Para corrigir essa inconsistência, é necessário realizar um **ajuste que atualiza apenas o saldo de rastreamento**, sem movimentar o estoque próprio e sem gerar impactos fiscais.

### **(1)** Passo a passo da configuração

**(1)** **Crie uma nova TOP de Ajuste**

**Configuração:**

- Não deve atualizar estoque próprio
- Não deve atualizar livros fiscais.

**Tipo de Movimento:**

- C – Compras (permitindo a entrada de saldo para o rastreamento).

(2)** Parametrização da TOP**

- Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências) e localize o parâmetro **"TOPENFNEISRAST".**

  - **Observação:** caso não exista o parâmetro, é preciso criá-lo.
- **Insira nesse parâmetro a TOP criada no passo anterior.**

**(3)** **Emissão do Documento de Ajuste**

- Utilize a TOP configurada para emitir um documento não fiscal;
- Informe o item e a quantidade que necessitam de ajuste no rastreamento e os valores de ST devidos;
- Ao confirmar, o sistema atualizará apenas o saldo de rastreamento (ST), sem alterar o estoque próprio.

**(4)** Execute a rotina **"Ativar/Reprocessar Rastreamento de Estoquer/ST".** Após essa ação é esperado que:

- O **saldo de rastreamento (ST)** seja corrigido;
- O **estoque próprio** permaneça inalterado;
- Não sejam gerados lançamentos fiscais ou contábeis indevidos.

### **(1)** Observações

- Esse procedimento deve ser utilizado **exclusivamente para ajustes de rastreamento;**
- Recomenda-se realizar testes em **ambiente de homologação** antes de aplicar em produção;
- Sempre alinhe esse processo com a **equipe fiscal e contábil** responsável.
