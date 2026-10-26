---
id: "39353028744599"
titulo: "Como exigir aprovação de compras por faixa de valor (Evento 44 e Liberação em Cascata)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39353028744599-Como-exigir-aprova%C3%A7%C3%A3o-de-compras-por-faixa-de-valor-Evento-44-e-Libera%C3%A7%C3%A3o-em-Cascata"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-10-08T19:16:00Z"
rotulos: ["Configuração", "Parceiro", "Workflow", "Liberação de Limites", "Artigo criado KCS", "CVE - KCS", "Compras"]
---

# Como exigir aprovação de compras por faixa de valor (Evento 44 e Liberação em Cascata)

O sistema permite exigir a **aprovação de um usuário liberador** nas compras, de acordo com **faixas de valor**. Esta funcionalidade é essencial para o **controle de alçadas** e a **governança de compras** na organização.

Nativamente, essa aprovação é feita com o **"Evento 44 - Liberação exigida pela TOP"**, junto com a **"Liberação em Cascata"**, que define quem aprova cada faixa de valor. Para estabelecer **valores específicos por comprador** (cada comprador com o seu próprio limite), é necessário criar uma **"Regra de Negócio"** personalizada, conforme explicado mais abaixo.

### Configuração do Evento 44 - Liberação exigida pela TOP e Liberação em Cascata

O **"Evento 44"** faz o sistema exigir liberação na confirmação de **toda nota** da TOP, independentemente do valor. A **"Liberação em Cascata"** define os níveis de aprovação: para cada faixa de valor da nota, qual usuário aprova e em que ordem.

Para configurar o evento de liberação:

**(1)**  Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências) e confirme que o parâmetro **"USALIBLIM - Usar liberação de limites por alçada?"** está ligado.
**(2)**  Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a TOP de compra.
**(3)**  Marque a opção **"Sempre exigir Liberação"**.
**(4)**  Na aba **"Liberação em Cascata"**, inclua o **"Evento 44"**.
**(5)**  Para cada nível de aprovação, informe a **"Ordem"**, a faixa de valor (**"Vlr. Mínimo"** e **"Vlr. Máximo"**) e quem aprova. Em **"Tipo"**, escolha um usuário específico ou o responsável pelo Centro de Resultado.
**(6)**  Verifique se cada usuário liberador tem **limite de liberação para o Evento 44** igual ou maior que o **"Vlr. Máximo"** da sua faixa. Sem esse limite, o sistema impede salvar a faixa ou exibe erro ao confirmar a nota.

### Alternativa: Regras de Negócio Personalizadas

Como a **liberação em cascata** trabalha com faixas de valor da nota, e não com limites por comprador, para ter **limites individuais por comprador** é necessário criar uma **"Regra de Negócio"** personalizada. O limite cadastrado no usuário para o evento define **até quanto ele pode aprovar** como liberador, e não até quanto ele pode comprar sem aprovação.

**Importante:** A **"Regra de Negócio"** não contempla automaticamente a funcionalidade de liberação em cascata, sendo necessário desenvolver a lógica que identifique o comprador, valide o valor da compra e acione o usuário liberador apropriado.

Esta solução permite trabalhar com múltiplos usuários liberadores diretamente na procedure, oferecendo maior flexibilidade para cenários complexos de aprovação.

### Exemplo de Aplicação Prática

Considere o seguinte cenário de limites por comprador, atendido pela **"Regra de Negócio"** personalizada:

- **Comprador 1:** Liberado para comprar até R$ 1.000,00
- **Comprador 2:** Liberado para comprar até R$ 2.000,00
- **Comprador 3:** Liberado para comprar até R$ 3.000,00

Sempre que o valor estabelecido para cada comprador for ultrapassado, o sistema acionará automaticamente um usuário liberador para avaliar e aprovar ou rejeitar a solicitação de compra.

Esta configuração garante o controle de alçadas e evita compras não autorizadas acima dos limites estabelecidos pela diretoria.
