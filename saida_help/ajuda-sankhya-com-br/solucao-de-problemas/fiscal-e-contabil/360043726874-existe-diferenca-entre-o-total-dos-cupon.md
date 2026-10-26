---
id: "360043726874"
titulo: "Existe diferença entre o total dos Cupons e a Redução Z, precisa rodar o utilitário que corrige a partir do MFD do ECF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043726874-Existe-diferen%C3%A7a-entre-o-total-dos-Cupons-e-a-Redu%C3%A7%C3%A3o-Z-precisa-rodar-o-utilit%C3%A1rio-que-corrige-a-partir-do-MFD-do-ECF"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:59:44Z"
rotulos: ["ECF", "Fast Service", "Atualização", "Diferença entre Cupons e Redução Z", "Divergência entre Totalizador e sistema", "Gere espelho MFD e compare dados", "SPED Fiscal", "Erro"]
---

# Existe diferença entre o total dos Cupons e a Redução Z, precisa rodar o utilitário que corrige a partir do MFD do ECF

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17799493295255) SITUAÇÃO:**

Ao gerar SPED Fiscal, e for constatada alguma divergência entre o total dos cupons e a Redução Z, será retornada a mensagem.

**![Imagem 2: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17799505638679) MENSAGEM:**

Existe diferença entre o total dos Cupons e a Redução Z, precisa rodar o utilitário que corrige a partir do MFD do ECF. Entre em contato com o suporte da Jiva.

Data: 10/12/2018 Redução Z: 1811 Máquina: 2 Cód.Empresa: 4 Vlr TGFLIV: 2614,94 Vlr TGFITE: 2613,37

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17799736284183) SOLUÇÃO:**

Conforme exemplo mencionado acima, a mensagem de erro apresenta a Data/Empresa/Máquina que apresentou a divergência.

![Imagem 4: Nessa máquina realize a geração do espelho MFD para o dia reportado:](https://ajuda.sankhya.com.br/hc/article_attachments/17799505648407) Nessa máquina realize a geração do espelho MFD para o dia reportado:

Utilitários » Impressora Fiscal » **Gerar Espelho MFD**

![Imagem 5: Inicie uma comparação entre os dados gravados no espelho e os dados gravados no sistema, para cada cupom dessa data.](https://ajuda.sankhya.com.br/hc/article_attachments/17799493320727) Inicie uma comparação entre os dados gravados no espelho e os dados gravados no sistema, para cada cupom dessa data.

**POSSÍVEIS DIVERGÊNCIAS:**

- ITEM cancelado no 'espelho' e existente no sistema
- CUPOM cancelado no 'espelho' e existente no sistema
- ITEM duplicado no sistema
- Desconto rateado no 'espelho' e não rateado no sistema

![Imagem 6: Identificada essa divergência, entre em contato com o Service Desk Sankhya Jiva para ajustes/correções.](https://ajuda.sankhya.com.br/hc/article_attachments/17799505661975) Identificada essa divergência, entre em contato com o Service Desk Sankhya Jiva para ajustes/correções.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17799505667351)CAUSA:**

- Essa mensagem representa uma divergência entre o Totalizador da redução Z da respectiva data, comparando com os valores apresentados para cada CUPOM desse dia em nosso sistema.
- Essa situação pode ocorrer por uma falha de comunicação da impressora fiscal, assim como dll's e/ou aplicativo do FAST desatualizado.
- Para uma tratativa da causa raiz aconselhamos manter a versão do FAST atualizada.
- Para correções pontuais, o Service Desk Sankhya Jiva dispões de um aplicativo que auxilia na identificação/correção dessa divergência, sendo esse utilizado apenas pela equipe de suporte e não disponibilizado aos clientes.
- Acima segue uma forma de adiantar a solução, que será viável caso a movimentação desse dia seja pequena.
