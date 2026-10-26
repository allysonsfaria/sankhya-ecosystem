---
id: "43546322057879"
titulo: "Desconto do Crédito Trabalhador valor da base margem incorreto."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43546322057879-Desconto-do-Cr%C3%A9dito-Trabalhador-valor-da-base-margem-incorreto"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-09-17T13:18:49Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Desconto do Crédito Trabalhador valor da base margem incorreto.

O desconto do **"Crédito Trabalhador"** base margem crédito trabalhador pode ficar incorreto devido à configuração  dos eventos que compõem a base de cálculo da margem consignável. É fundamental que todos os eventos utilizados na rescisão estejam devidamente vinculados à base de margem do crédito do trabalhador para que o desconto seja processado corretamente pelo sistema.

Quando a base de margem não está configurada corretamente nos eventos personalizados ou padrão utilizados na folha  , o sistema não reconhece os valores como parte da remuneração disponível para desconto, impedindo o cálculo correto do desconto do empréstimo consignado do trabalhador.

### Como ajustar a base de margem para o desconto

Para que o desconto do **"Crédito Trabalhador"** seja calculado corretamente na rescisão, siga os passos abaixo:

**(1)** Acesse a tela de **"Eventos"** Pessoal+ » Cadastros » Eventos e localize todos os eventos utilizados na folha     como **"Saldo Salário Rescisão"**, **"Saldo Banco de Horas"** e **"DSR Saldo Banco de Horas"**.
**(2)** Verifique se cada evento está configurado para compor a base de margem do crédito do trabalhador equivalente. 
**(3)** Caso utilize eventos personalizados, insira manualmente a base de margem do crédito do trabalhador nesses eventos.

![Imagem 1: (1) Acesse a tela de "Eventos" Pessoal+ » Cadastros » Eventos e localize todos os eventos utilizados na folha como…](https://ajuda.sankhya.com.br/hc/article_attachments/43558766105623)

**(4)** Após o ajuste, recalcule a rescisão para validar se o desconto do crédito trabalhador foi apresentado corretamente.

Ao seguir esses passos, o sistema irá considerar corretamente os valores para o cálculo do desconto do crédito trabalhador.

### Principais causas do não cálculo automático

Os principais motivos para o desconto do **"Crédito Trabalhador"** não ser calculado automaticamente na rescisão são:

- Eventos padrão ou personalizados não configurados para compor a base de margem do crédito do trabalhador.
- Utilização de eventos desprotegidos ou desvinculados da base de margem.
- Importação manual do empréstimo sem o devido vínculo com a base de cálculo.

Artigo relacionado:

<https://ajuda.sankhya.com.br/hc/pt-br/articles/39352477406743-Como-configurar-eventos-na-base-de-c%C3%A1lculo-da-margem-consign%C3%A1vel-para-empr%C3%A9stimo-consignado-em-rescis%C3%A3o>

Ao identificar e corrigir essas situações, o desconto será processado corretamente na folha de rescisão.

### Validação do cálculo após ajuste

Após realizar os ajustes necessários nos eventos e recalcular a folha, valide se o desconto do **"Crédito Trabalhador"** está sendo apresentado corretamente na folha. Caso o desconto ainda não apareça, revise novamente a configuração dos eventos e a vinculação à base de margem.

A correta configuração garante o cumprimento da legislação e evita divergências no cálculo do desconto consignado na rescisão.
