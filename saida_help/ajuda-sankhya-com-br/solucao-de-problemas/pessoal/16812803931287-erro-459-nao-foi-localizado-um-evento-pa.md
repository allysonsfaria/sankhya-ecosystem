---
id: "16812803931287"
titulo: "Erro 459 - Não foi localizado um evento para o recibo de entrega informado ou o mesmo foi excluído/retificado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16812803931287-Erro-459-N%C3%A3o-foi-localizado-um-evento-para-o-recibo-de-entrega-informado-ou-o-mesmo-foi-exclu%C3%ADdo-retificado"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-14T20:00:11Z"
rotulos: ["Eventos", "Central de Vendas", "XML", "eSocial", "Erro 459", "Recibo de entrega inválido ou excluído", "Evento ou recibo não localizado", "Verificar recibo no eSocial ou contatar Service Desk", "Erro", "Artigo atualizado KCS", "Sankhya RH - KCS"]
---

# Erro 459 - Não foi localizado um evento para o recibo de entrega informado ou o mesmo foi excluído/retificado

**MENSAGEM**

[459] - Não foi localizado um evento para o recibo de entrega informado ou o mesmo foi excluído/retificado.

Deverá existir um evento já recebido, **"Ativo"** (não excluído ou retificado), com número de recibo de entrega igual ao informado no campo.

**SITUAÇÃO**

Ao tentar enviar eventos para o eSocial (como S-2200, S-2206, entre outros), o sistema apresenta o erro 459, impedindo o envio da alteração ou exclusão do evento. Esta situação ocorre quando o sistema tenta referenciar um recibo que não existe mais no portal do eSocial ou quando há divergência entre os recibos cadastrados no sistema e os recibos efetivamente registrados no portal.

**SOLUÇÃO:**

Verifique na tabela do evento que apresentou o erro e confirme se o recibo mencionado corresponde ao registrado no portal do eSocial.
Caso haja divergência, entre em contato com o Service Desk para que o motivo da inconsistência seja analisado.

**CAUSA**

O erro 459 ocorre devido a inconsistências entre os recibos cadastrados no sistema e os recibos efetivamente registrados no portal do eSocial. As principais causas incluem:

- **Evento excluído ou retificado no portal:** o evento foi excluído ou retificado diretamente no portal do eSocial, mas o sistema ainda mantém o recibo antigo cadastrado.
- **Recibos de produção restrita:** foram inseridos recibos de produção restrita (iniciados com "1.2") que não são válidos para o ambiente de produção.
- **Perda de sincronização:** houve perda de sincronização entre o sistema e o portal do eSocial, fazendo com que os recibos fiquem divergentes.
