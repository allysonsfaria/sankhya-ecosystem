---
id: "20342186373911"
titulo: "ORA-01400: não é possível inserir NULL em (\"SANKHYA\".\"TGWITT\".\"CODENDDESTINO\")"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20342186373911-ORA-01400-n%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-NULL-em-SANKHYA-TGWITT-CODENDDESTINO"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:51:09Z"
rotulos: ["Configuração", "WMS", "Estoque", "Preferências", "Erro: NULL em \"CODENDDESTINO\"", "Cancelamento de expedição", "Configure \"Endereço Indefinido\"", "Erro"]
---

# ORA-01400: não é possível inserir NULL em ("SANKHYA"."TGWITT"."CODENDDESTINO")

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/20342201201943) **MENSAGEM:**

ORA-01400: não é possível inserir NULL em ("SANKHYA"."TGWITT"."CODENDDESTINO").

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/20342201206295)CAUSA:**

Ao cancelar uma expedição pela rotina de expedição de mercadorias - botão outras opções 'Cancelar separação' ou quando a expedição já está cancelada, mas, no coletor de dados é necessário gerar a tarefa de retorno das mercadorias, através da tarefa subsequente ao momento que foi cancelada a expedição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20342186369815)SOLUÇÃO:**

Quando o parâmetro **"Utiliza lote único por endereço? - LOTEUNICOXEND"** está habilitado, é necessário configurar nas [preferências da empresa no](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa) campo **"Cód. End. Armazenamento Indefinido"**indique um endereço de armazenamento indefinido que é utilizado durante a geração de tarefas de armazenagem, quando nenhuma regra de armazenagem é satisfeita. Deste modo, é gerada tarefa com a quantidade restante a armazenar para o endereço definido neste campo.

![Imagem 4: Quando o parâmetro "Utiliza lote único por endereço? - LOTEUNICOXEND" está habilitado, é necessário configurar nas…](https://ajuda.sankhya.com.br/hc/article_attachments/20440559830039)
