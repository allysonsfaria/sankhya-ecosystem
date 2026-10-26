---
id: "39371605975191"
titulo: "Desconto duplicado de IRRF no 13º salário na rescisão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39371605975191-Desconto-duplicado-de-IRRF-no-13%C2%BA-sal%C3%A1rio-na-rescis%C3%A3o"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-26T00:03:41Z"
rotulos: ["Configuração", "Atualização", "Impostos", "Folha", "Rescisão", "IRRF", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Desconto duplicado de IRRF no 13º salário na rescisão

**Mensagem**

O sistema está descontando o IRRF do 13º salário duas vezes: uma vez na folha de 13º salário e novamente no cálculo da rescisão.

**Situação**

Ao processar o cálculo de rescisão de um colaborador que já teve o **"13º salário calculado"** e o **"IRRF retido"** na folha específica de 13º, o sistema está processando o 13º salário complementar corretamente na rescisão. Contudo, no cálculo do IRRF da rescisão, o sistema não está deduzindo o valor do imposto já retido anteriormente, efetuando o desconto integral novamente.

**Solução**

Para corrigir o desconto duplicado do IRRF do 13º salário na rescisão, siga os passos abaixo:

**(1)** Verifique se a fórmula do **"Evento 9060"** (IRRF 13º Salário) está configurada corretamente. Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento **"9060"**.

![Imagem 1: Certifique-se de que a fórmula do evento está padronizada (se for este o caso, estará na aba: 'fórmula padrão, conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/41260422181783)

**(2)** Certifique-se de que a fórmula do evento está padronizada **(se for este o caso, estará na aba: 'fórmula padrão, conforme a demonstração abaixo)** ante a configuração padrão do sistema. Se a fórmula estiver personalizada ou fora do padrão, ajuste-a para a fórmula padrão.

1º Acesse a aba 'básico' e identifique a fórmula utilizada neste evento:

![Imagem 2: 1º Acesse a aba 'básico' e identifique a fórmula utilizada neste evento:](https://ajuda.sankhya.com.br/hc/article_attachments/41260429060247)

2º Na tela: Fórmulas (Pessoal+ » Cadastros » Fórmulas) verifique a fórmula localizada:

![Imagem 3: 2º Na tela: Fórmulas ( Pessoal+ » Cadastros » Fórmulas) verifique a fórmula localizada:](https://ajuda.sankhya.com.br/hc/article_attachments/41260422185239)

**(3)** Verifique se o sistema está na versão de módulo Pessoal+/W mais recente, pois versões anteriores podem apresentar inconsistências no cálculo de recomposição do IRRF do 13º salário na rescisão.

**Para verificar as últimas versões disponíveis acesse: https://downloads.sankhya.com.br/consulta-versao?c=1**

**(4)** Caso necessário, solicite a atualização do sistema para a versão estável mais recente que contempla a correção deste cálculo.

**Para o passo a passo de atualização, veja: https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-Om-via-WPM**

**(5)** Após os ajustes, exclua o cálculo da rescisão e processe-o novamente para que o sistema recalcule corretamente o IRRF, deduzindo o valor já retido na folha de 13º salário.

**(6)** Valide o cálculo verificando se o sistema está descontando apenas a diferença do IRRF e não o valor total novamente.

**Causa**

O problema ocorre quando a fórmula do **"Evento 9060"** está fora do padrão ou personalizada de forma incorreta, impedindo que o sistema realize a recomposição adequada do IRRF do 13º salário na rescisão. Além disso, versões do sistema anteriores podem apresentar falhas no cálculo de dedução do imposto já retido, causando o desconto duplicado.

O cálculo correto deve considerar o IRRF já descontado na folha de 13º salário e aplicar apenas a diferença, se houver, no momento da rescisão, evitando a bitributação do colaborador.
