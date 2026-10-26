---
id: "39352475984535"
titulo: "Erro na Geração S-2240 | ORA-00001: Restrição Exclusiva (SANKHYA.PK TFPS2240AGNOC.EPI) Violada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39352475984535-Erro-na-Gera%C3%A7%C3%A3o-S-2240-ORA-00001-Restri%C3%A7%C3%A3o-Exclusiva-SANKHYA-PK-TFPS2240AGNOC-EPI-Violada"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-16T13:22:47Z"
rotulos: ["Configuração", "Atualização", "Pessoal", "eSocial", "Central do eSocial", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro na Geração S-2240 | ORA-00001: Restrição Exclusiva (SANKHYA.PK TFPS2240AGNOC.EPI) Violada

**MENSAGEM**

ORA-00001: restrição exclusiva (SANKHYA.PK TFPS2240AGNOC.EPI) violada

**SITUAÇÃO**

Ao tentar gerar o evento **"S-2240"**, o sistema apresenta erro de violação de restrição exclusiva. Este erro ocorre após atualização do módulo Pessoal, impedindo a geração correta dos eventos do eSocial.

**SOLUÇÃO**

Para resolver este erro, siga os passos abaixo:

**(1)** Acesse a tela **"Ambiente de Trabalho"** (Pessoal+ » Rotinas Folha » SESMT » Ambiente de Trabalho) e verifique se há funcionários cadastrados em ambientes duplicados.

![Imagem 1: Identifique se existe mais de um ambiente cadastrado para o mesmo funcionário com a mesma data de início de condição.…](https://ajuda.sankhya.com.br/hc/article_attachments/41274326057111)

**(2)** Identifique se existe mais de um ambiente cadastrado para o mesmo funcionário com a mesma data de início de condição. Para isso basta acessar tela **"Configuração Funcionários"** (Configurações » Cadastros » Pessoal » Configuração Funcionários) aba Ambiente de Trabalho.

![Imagem 2: Verifique se os ambientes duplicados utilizam o mesmo agente nocivo e possuem o cadastro dos mesmos EPIs.](https://ajuda.sankhya.com.br/hc/article_attachments/41329841019927)

**(3)** Verifique se os ambientes duplicados utilizam o mesmo agente nocivo e possuem o cadastro dos mesmos EPIs.

![Imagem 3: (3) Verifique se os ambientes duplicados utilizam o mesmo agente nocivo e possuem o cadastro dos mesmos EPIs.](https://ajuda.sankhya.com.br/hc/article_attachments/41329856298007)

**(4)** Exclua o ambiente incorreto ou duplicado, mantendo apenas o registro válido para o funcionário.

**(5)** Realize uma nova geração do evento **"S-2240"** e verifique se o erro foi solucionado.

**CAUSA**

O erro ocorre devido à duplicidade de registros no cadastro de ambientes de trabalho. Quando um funcionário está cadastrado em dois ambientes diferentes com o mesmo início de condição, utilizando o mesmo agente nocivo e os mesmos EPIs.

Esta situação é mais comum após atualizações do módulo Pessoal, quando podem ocorrer inconsistências nos cadastros de ambientes de trabalho.
