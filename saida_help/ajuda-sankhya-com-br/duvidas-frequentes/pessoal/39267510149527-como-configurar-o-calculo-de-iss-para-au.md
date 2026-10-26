---
id: "39267510149527"
titulo: "Como configurar o cálculo de ISS para autônomos no RPA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39267510149527-Como-configurar-o-c%C3%A1lculo-de-ISS-para-aut%C3%B4nomos-no-RPA"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:33Z"
rotulos: ["ISS", "Configuração", "Alíquota de ISS", "Cidades", "Impostos", "Artigo criado KCS", "Sankhya RH - KCS", "RPA"]
---

# Como configurar o cálculo de ISS para autônomos no RPA

O **"ISS"** (Imposto Sobre Serviços) para autônomos deve ser calculado automaticamente ao processar o **"RPA"** (Recibo de Pagamento a Autônomo). Quando o sistema não realiza esse cálculo, é necessário verificar a configuração do evento de ISS e sua fórmula de cálculo.

Este artigo orienta sobre como configurar corretamente o evento de ISS para que o cálculo seja realizado de forma automática durante o processamento do RPA.

### Configuração do evento de ISS

Para que o ISS seja calculado corretamente no RPA, é necessário criar ou ajustar um evento específico com as configurações adequadas.

**(1)** Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e crie um novo evento ou localize o evento existente para ISS de autônomos.

**(2)** No campo **"Regra de Cálculo"**, marque as opções **"Normal"** e **"Rescisão"** para que o evento seja considerado em ambos os tipos de folha.

**(3)** No campo **"Índice"**, insira o percentual aplicado pela sua empresa (por exemplo, **0,05** para 5%).

**(4)** No campo **"Identificação"**, insira o código **198**, que corresponde ao evento de ISS autônomos movimento.

### Alíquota do ISS

A alíquota varia conforme o município (geralmente entre 2% e 5%). Verifique a legislação municipal aplicável antes de configurar a fórmula.

#### ⚠️O evento 9350 (padrão) - ISS AUTONOMOS MOV  é possível efetuar alterações do valor do índice, devido imposto varia de acordo com região e cidade .

### Processamento automático do cálculo

Após realizar as configurações do evento, o **"ISS"** será calculado automaticamente durante o processamento do RPA, sem a necessidade de lançamento manual.

Ao processar o cálculo do RPA, verifique se o evento de ISS aparece automaticamente na folha de pagamento do autônomo. Caso o evento não seja calculado, revise as configurações realizadas, especialmente a fórmula vinculada e o índice aplicado.

### Verificação do índice correto

É fundamental garantir que o **"Índice"** do ISS esteja configurado corretamente no evento. Caso o índice esteja incorreto (por exemplo, **0,04** ao invés de **0,05**), o cálculo será realizado com o percentual errado.

Acesse novamente o evento de ISS e confirme se o valor no campo **"Índice"** corresponde ao percentual praticado pela sua empresa. Após o ajuste, reprocesse o cálculo do RPA para validar a correção.
