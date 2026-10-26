---
id: "31256288346391"
titulo: "IPI pode impactar o recálculo de descontos nas operações. Conheça o movito e a solução para essa divergência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31256288346391-IPI-pode-impactar-o-rec%C3%A1lculo-de-descontos-nas-opera%C3%A7%C3%B5es-Conhe%C3%A7a-o-movito-e-a-solu%C3%A7%C3%A3o-para-essa-diverg%C3%AAncia"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:33:27Z"
rotulos: ["Configuração", "IPI", "Impostos", "TOP", "Desconto", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "solução", "comum surgirem inconsistências no valor do desconto", "realiza o cálculo do desconto nesses momentos", "IPI pode impacta", "recálculo de descontos nas operações", "operações fiscais que envolvem IPI", "incluir ou alterar um item na nota", "divergência ocorre devido à forma como o sistema Sankhya"]
---

# IPI pode impactar o recálculo de descontos nas operações. Conheça o movito e a solução para essa divergência

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31256288337687) **MENSAGEM:**

Em operações fiscais que envolvem IPI, é comum surgirem inconsistências no valor do desconto ao incluir ou alterar um item na nota. Essa divergência ocorre devido à forma como o sistema Sankhya realiza o cálculo do desconto nesses momentos.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31256288338455)SOLUÇÃO:**

Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências) e ative o parâmetro **"Calcular % desconto sem impostos? - PERCSEMIMP". Assim,** **independentemente da presença ou valor do IPI, o problema será resolvido**. Pois, essa configuração garante que o sistema utilize um valor de referência consistente para o cálculo do desconto, evitando variações inesperadas.

####

#### Entenda o cenário

Ao modificar o **Percentual de Desconto** de um item durante a inclusão ou edição, o sistema executa duas ações automaticamente:

(1)** Zera os impostos** (se a TOP não estiver configurada como "Não calcula e digita");

(2)** Recalcula o valor do desconto** com base em um valor total de referência.

O valor total de referência utilizado no cálculo depende de quatro possíveis cenários, tratados na rotina **"recalculaValorDesconto"**:

(2)** Parâmetro ''**PERCSEMIMP'' **ativado:** valor de referência = VLRTOT – Valor dos serviços

(2)** Parâmetro "TIPTABPRECOS" configurado como 9 (parceiro tabela) e não se trata de uma compra:** valor de referência = VLRTOT + VLRIPI + VLRSUBST – Valor dos serviços – VLRREPRED

(2)**Campo “Soma ST no total da nota” ativado na TOP:** valor de referência = VLRTOT + VLRIPI + VLRSUBST – Valor dos serviços

(2)** Demais casos:** valor de referência = VLRTOT + VLRIPI – Valor dos serviços

#### Exemplo Prático

Temos os seguintes dados:

- **VLRTOT:** R$ 7.630,00
- **VLRIPI:** R$ 388,82
- **TOP:** configurada para somar o IPI ao total da nota.

Logo, o valor de referência para o desconto será: **R$ 7.630,00 + R$ 388,82 = R$ 8.018,82**
Aplicando 2% de desconto: **8.018,82 × 2% = R$ 160,37**

O valor exibido foi **R$ 160,40 no campo** "Vlr Desconto", o que é explicado por parâmetros de arredondamento, como **"ARREDDESCITE"**.

#### Por que o desconto aparece como R$ 152,60 na edição do item?

Isso ocorre porque, ao alterar um item, o sistema **zera os impostos temporariamente** para recálculo. Nesse momento, o campo **VLRIPI está zerado**, o que altera o valor de referência para o desconto, gerando um valor diferente (R$ 152,60).

Mesmo que a TOP esteja configurada para somar o IPI, **sem o parâmetro ''**PERCSEMIMP'' **ativado**, o sistema considera esse valor zerado no momento da edição.

**OBSERVAÇÃO:**

O parâmetro ''PERCSEMIMP'' existe apenas no **Pedido de Compra/Venda**. Na **Cotação de Compras** não existe preferência equivalente: o cálculo é fixo e sempre soma o IPI antes de aplicar o desconto ao item.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31256331884695)CAUSA:**

O valor do IPI **só será considerado** se, na TOP da nota, a opção **“Somar IPI ao total da nota”** estiver ativada. Caso contrário, o sistema o ignora no cálculo do desconto.

Para garantir consistência no valor do desconto, principalmente em operações com IPI, recomenda-se **ativar o parâmetro ''**PERCSEMIMP'' . Isso assegura que o cálculo do desconto utilize um valor de referência sem a influência transitória dos impostos, evitando divergências e retrabalho.
