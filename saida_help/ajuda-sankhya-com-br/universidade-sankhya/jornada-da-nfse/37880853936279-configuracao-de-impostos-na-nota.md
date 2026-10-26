---
id: "37880853936279"
titulo: "Configuração de impostos na nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880853936279-Configura%C3%A7%C3%A3o-de-impostos-na-nota"
trilha: "Universidade Sankhya > Jornada da NFSe"
atualizado_em: "2026-07-22T14:06:21Z"
rotulos: ["Configuração", "XML", "Impostos", "Preferências", "Financeiro", "NFS-e"]
---

# Configuração de impostos na nota

## Tratamento do imposto na nota

Após definir os critérios de cálculo e retenção, a escolha entre destacar ou reter impostos determina como a NFS-e será formada e como o financeiro seguirá.

Quando destacados na nota, os tributos ficam demonstrados no XML/RPS e o total permanece bruto; a dedução ocorre no financeiro, na liquidação do título.

Quando retidos na nota, os valores são abatidos do total da NFS-e, o XML/RPS já reflete a retenção e o financeiro nasce líquido.

Essa coerência entre nota e financeiro evita divergências com o cliente, retrabalho na baixa e rejeições por inconsistência. Misturar as duas lógicas no mesmo fluxo tende a gerar dupla retenção e diferenças de valores.

#### Siga as orientações para realizar a configuração no ERP Sankhya

1. Acesse a tela **Preferências**

**Menu:** Configuração  »  Avançado  »  Preferências

- Digite o parâmetro no campo (Chave ou Descrição e tecle ENTER) e pressione **ENTER** para carregar as informações.
- Ative ou desligue o parâmetro de acordo com sua necessidade.

#### Parâmetros de geração e retenção de impostos

Dois parâmetros controlam o comportamento dos impostos:

- **GERIMPOSTO**: define se os impostos serão gerados no financeiro.
  Gerar impostos (ISS, INSS, IRF) no financeiro?
- **CONSIMPRETNOTA**: define se os impostos serão retidos diretamente na nota.
  Considerar impostos retidos no valor da nota?

As combinações possíveis são:

1. **GERIMPOSTO = S e CONSIMPRETNOTA = N**
   Os impostos são gerados no momento da baixa.
   A nota e o financeiro permanecem com o valor cheio, sem retenção.
2. **GERIMPOSTO = N e CONSIMPRETNOTA = S**
   A retenção ocorre na própria nota.
   O financeiro já sai líquido, com a retenção descontada.
   Na baixa não há nova retenção, pois ela já foi aplicada.
   Observação: a nota precisa estar confirmada para que o cálculo seja realizado.
3. **GERIMPOSTO = N e CONSIMPRETNOTA = N**
   O sistema calcula os impostos como retidos, mas não gera financeiro.
   A nota e o financeiro ficam com o valor cheio.
   Na baixa é possível desmarcar “Retido” e zerar os valores dos impostos.
4. **GERIMPOSTO = S e CONSIMPRETNOTA = S**
   Essa combinação não é permitida.
   Ao acessar a Central (Compras, Vendas ou Movimentações Internas), o sistema apresenta mensagem de alerta.
