---
id: "36263765443991"
titulo: "As seguintes TOPs não possuem configuração de contabilização e impediram o processamento de XX registros: XX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36263765443991-As-seguintes-TOPs-n%C3%A3o-possuem-configura%C3%A7%C3%A3o-de-contabiliza%C3%A7%C3%A3o-e-impediram-o-processamento-de-XX-registros-XX"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-09-17T13:35:17Z"
rotulos: ["Configuração", "Filtros", "TOP", "Contabilização", "Financeiro", "Configurações de TOPs", "Parâmetros de Contabilização", "Erro", "TOP Contabilização", "Configuração de Contabilização"]
---

# As seguintes TOPs não possuem configuração de contabilização e impediram o processamento de XX registros: XX

**MENSAGEM:**

As seguintes TOPs não possuem configuração de contabilização e impediram o processamento de XX registros: XX

**SOLUÇÃO:**

**(1)** Verifique na tela [**''TOP Contabilização'**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o)' e confirme se as TOPs possuem fórmula de contabilização configuradas.

**(2)** Se não houver nenhuma fórmula vinculada, cadastre ao menos uma regra contábil, pois ela é necessária para que o processamento seja concluído.

**(3)** Em seguida, acesse a tela [**''Agendamentos''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608294-Agendamento) (Contabilização » Rotinas » Agendamento), abra a aba **“Filtros”** e revise a seção [**“Parâmetros de Contabilização”**](https://ajuda.sankhya.com.br/hc/pt-br/articles/27390133571991-Par%C3%A2metros-de-Contabiliza%C3%A7%C3%A3o)**.**

**(4)** Caso exista algum filtro configurado que esteja eliminando todas as fórmulas das TOPs, ajuste ou remova.

Filtros restritivos podem fazer com que o sistema não encontre nenhuma fórmula válida, mesmo quando elas existem.

**CAUSA:**

A mensagem ocorre, geralmente, por dois motivos:

- **TOP sem fórmulas de contabilização:**

Durante o processamento da tela ''Agendamento'' **(**Contabilização » Rotinas » Agendamento), o sistema identifica documentos aptos a serem contabilizados, mas ao verificar a TOP vinculada, não encontra nenhuma fórmula cadastrada na tela ''TOP Contabilizações'' **(**Contabilização » Arquivos » TOP Contabilização).

Nesse caso, o sistema entende que não há regra contábil para executar.

- **Filtros que eliminam as fórmulas existentes:**

Na tela ''Agendamento'', aba ''**Filtros''**, a seção ''Parâmetros de Contabilização'' permite aplicar filtros sobre as fórmulas das TOPs.

Se algum filtro criado resultar em **nenhuma fórmula retornada,** mesmo que existam fórmulas configuradas, o sistema interpreta que não existe fórmula válida.

Assim, é necessário revisar ou remover o filtro que está restringindo incorretamente as regras de contabilização.

![Imagem 1: Assim, é necessário revisar ou remover o filtro que está restringindo incorretamente as regras de contabilização.](https://ajuda.sankhya.com.br/hc/article_attachments/36421267437079)
