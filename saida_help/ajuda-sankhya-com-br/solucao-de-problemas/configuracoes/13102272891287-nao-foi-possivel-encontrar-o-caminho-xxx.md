---
id: "13102272891287"
titulo: "Não foi possível encontrar o caminho XXXXXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13102272891287-N%C3%A3o-foi-poss%C3%ADvel-encontrar-o-caminho-XXXXXXX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:00:25Z"
rotulos: ["Configuração", "Servidor", "Repositório", "CORE_E01751", "Parâmetro", "Caminho Ausente: Verificação e Solução", "Erro"]
---

# Não foi possível encontrar o caminho XXXXXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17295656916631) MENSAGEM:**

 [CORE\_E01751]: Não foi possível encontrar o caminho XXXXXXX.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17295673358359) SOLUÇÃO:**

Verifique os parâmetros abaixo para validação da correta configuração (a frente dos parâmetros tem suas configurações):
 
**"SERVDIRMOD"**: /home/mgeweb/repositorio/impressao/
 
**"FREPBASEFOLDER"**: /home/sdeteste29/

Repositório:     -----------------
 
Assim identificamos a divergência do caso, pois essa é a forma de validar as configurações de busca dos arquivos dentro do sistema: FREPBASEFOLDER + Repositório= SERVDIRMOD. Entretanto, caso o FREPBASEFOLDER esteja em desacordo com o SERVDIRMOD é recomendável que reveja dentro do Servidor se esse caminho descritos no parâmetro FREPBASEFOLDERexiste de fato.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17295673359511)CAUSA:**

Ocorre quando há uma divergência entre as configurações de busca dos arquivos dentro do sistema: FREPBASEFOLDER + Repositório= SERVDIRMOD.
