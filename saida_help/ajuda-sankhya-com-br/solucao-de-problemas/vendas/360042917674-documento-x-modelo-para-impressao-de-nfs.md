---
id: "360042917674"
titulo: "Documento 'X': Modelo para impressão de NFS-e não configurado para a TOP 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042917674-Documento-X-Modelo-para-impress%C3%A3o-de-NFS-e-n%C3%A3o-configurado-para-a-TOP-Y"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:56Z"
rotulos: ["#PUBLIFER", "CORE_E05227", "Configuração", "Impressão", "Relatórios Formatados", "Cidades", "TOP", "NFS-e", "Erro Modelo Impressão", "Cadastramento de Modelos", "Configuração Tipos de Operação"]
---

# Documento 'X': Modelo para impressão de NFS-e não configurado para a TOP 'Y'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16117392381207) MENSAGEM:**

[CORE\_E05227] Documento 'X': Modelo para impressão de NFS-e não configurado para a TOP 'Y'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16117376060695) SOLUÇÃO:**

![Imagem 3: Acesse a tela 'Tipos de Operação' (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) ;](https://ajuda.sankhya.com.br/hc/article_attachments/16117392394263) Acesse a tela 'Tipos de Operação' (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP);

![Imagem 4: Selecione o 'Cód.TOP' utilizado no lançamento da respectiva NFS-e;](https://ajuda.sankhya.com.br/hc/article_attachments/16117392400663) Selecione o 'Cód.TOP' utilizado no lançamento da respectiva NFS-e;

![Imagem 5: Na aba 'NFS-e' verifique se os campos abaixo encontram-se devidamente configurados:](https://ajuda.sankhya.com.br/hc/article_attachments/16117392403095) Na aba 'NFS-e' verifique se os campos abaixo encontram-se devidamente configurados:

![Imagem 6: Na aba 'NFS-e' verifique se os campos abaixo encontram-se devidamente configurados:](https://ajuda.sankhya.com.br/hc/article_attachments/14606243511447)

(2)** Cód. Mod. Imp. NFSe:** Previamente deve-se cadastrar na tela Modelos de Nota Fiscal/Duplicatas/Boleto(s) um modelo para ser configurado para esta.  A NFS-e não utilizará o DANFE. O modelo de impressão é livre, ou seja, cada empresa fará seu modelo em “Relatórios Formatados” ou “TXT” de acordo com a legislação de cada cidade.

**Exemplo:** No caso da cidade de Aparecida de Goiás, existe um modelo pré-estabelecido. Já no caso da cidade de Belo Horizonte não existe nada na legislação sobre o padrão de impressão, portanto ficará a critério do cliente.

(2)** Cód. Mod. Imp. RPS:** Previamente deve-se cadastrar na tela Modelos de Nota Fiscal/Duplicatas/Boleto(s) um modelo para ser configurado para esta. Este será usado no caso de contingência, quando o serviço de NFS-e estiver fora do ar. Este modelo de impressão também é livre. Cada empresa terá seu **Modelo de impressão de RPS** em **Relatórios Formatados** ou **TXT** de acordo com a legislação de cada cidade. O sistema usará o modelo de RPS quando a nota for marcada para RPS a pedido do usuário.

**Nota:** O RPS tem a função de um DANFE de Segurança.

![Imagem 7: Realizado as configurações acima, refaça o teste de impressão.](https://ajuda.sankhya.com.br/hc/article_attachments/16117392415895) Realizado as configurações acima, refaça o teste de impressão.

**![Imagem 8: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17804161253399) IMPORTANTE:**

A criação/configuração de tais modelos não é realizada pelo Service Desk, e deverá ser validada junto aos consultores de sua Filial.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16117376095639) CAUSA:**

Ao realizar tentativa de impressão de NFS-e, sem que as devidas configurações de modelo de impressão tenham sido realizadas, será retornada a mensagem.
