---
id: "38911965262871"
titulo: "Guia: Configuração da Função \"N/A\" no Aplicativo SOP Logística"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38911965262871-Guia-Configura%C3%A7%C3%A3o-da-Fun%C3%A7%C3%A3o-N-A-no-Aplicativo-SOP-Log%C3%ADstica"
trilha: "Sankhya Official Pack - SOP > SOP"
atualizado_em: "2026-07-22T14:00:56Z"
rotulos: ["Configuração", "Aplicativo", "APP SOP Logística", "N/A", "Não se aplica", "Backend", "Cadastro de Itens do Checklist", "Modelos de Checklist", "Habilitar N/A", "Logística", "SOP Logística", "Checklist"]
---

# Guia: Configuração da Função "N/A" no Aplicativo SOP Logística

Agora, o **aplicativo SOP Logística** permite que o usuário **marque através de um campo** os itens de um checklist como **"N/A" (Não se Aplica)** durante a execução de uma atividade.

Essa nova funcionalidade tem como objetivo **permitir que o usuário indique quando um item não é pertinente à atividade** que está realizando no momento.

#### Como funciona na prática?

**No APP:**

**Durante a execução de um checklist**, um novo campo de marcação identificado como "N/A" é exibido ao lado de cada item. O comportamento do sistema baseia-se nos seguintes pilares:

- Quando um item não é pertinente à atividade atual, a seleção da opção "N/A" indica que aquele requisito **não deve ser considerado**.
- Uma vez assinalado como "N/A", o **sistema desabilita automaticamente as exigências de preenchimento ou validação**, como a inclusão obrigatória de fotos ou observações.
- O fluxo de execução **permite o avanço para a próxima etapa do checklist** de forma fluida, sem que o sistema aponte pendências ou impeça a finalização do item específico.

![Imagem 1: O fluxo de execução permite o avanço para a próxima etapa do checklist de forma fluida, sem que o sistema aponte…](https://ajuda.sankhya.com.br/hc/article_attachments/38911965260183)

**No Registro do Sistema (Backend):**

- A marcação de "N/A" é persistida no banco de dados para o item correspondente, assegurando o histórico da operação.
- O sistema não exige a validação do modelo de checklist para os itens marcados. Isso significa que as regras de obrigatoriedade (como fotos ou campos de texto) são ignoradas pelo servidor quando a opção "N/A" está selecionada

#### Procedimento de Configuração

##### **(1)** Acesse a tela ''Cadastro de Itens do Checklist'' (Logística » Gestão de Frotas » Checklist Operacional » Modelo de Checklist Operacional » Cadastro de Itens do Checklist).

**(1)** Na aba **''Geral''**, localize o campo **''Habilitar N/A''**.

**(1)** Habilite o parâmetro.

**OBSERVAÇÃO**: Caso a opção esteja desmarcada a opção de “N/A” não será exibida no Aplicativo do checklist. 

![Imagem 2: OBSERVAÇÃO : Caso a opção esteja desmarcada a opção de “N/A” não será exibida no Aplicativo do checklist.](https://ajuda.sankhya.com.br/hc/article_attachments/38911965257367)![Imagem 3: OBSERVAÇÃO : Caso a opção esteja desmarcada a opção de “N/A” não será exibida no Aplicativo do checklist.](https://ajuda.sankhya.com.br/hc/article_attachments/38911924690967)

**(1)** Após a configuração, acesse o aplicativo e verifique os itens do checklist configurados para essa funcionalidade.
