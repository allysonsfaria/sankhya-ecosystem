---
id: "4411944197399"
titulo: "Evento S-1200 no ambiente de E-Social com valor diferente para Plano de Saúde"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4411944197399-Evento-S-1200-no-ambiente-de-E-Social-com-valor-diferente-para-Plano-de-Sa%C3%BAde"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:36:23Z"
rotulos: ["Configuração", "Eventos", "Folha", "não apagar", "eSocial", "Exclua e reenvie S-1200 ajuste liberação da folha", "Evento S-1200 mostra desconto incorreto", "Tabelas TFPTVPS e TFPVPS não atualizadas", "Central de Projetos"]
---

# Evento S-1200 no ambiente de E-Social com valor diferente para Plano de Saúde

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16147383828631) MENSAGEM**:

Ao enviar o evento S-1200 e verificar no ambiente de E-Social, está sendo descontado apenas R$ 2,00 para os colaboradores.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16147383837079) CAUSA:**

As tabelas TFPTVPS e TFPVPS são alimentadas com a liberação da folha.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16147383844119) SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![Imagem 4: Gerar a excluir o S1200 já enviado ao esocial;](https://ajuda.sankhya.com.br/hc/article_attachments/16147356612375) Gerar a excluir o S1200 já enviado ao esocial;

| - MGE **Pessoal>>Avançado>> Liberar o envio da folha ao esocial;** - Desmarque a folha e a deixe como não liberada ao esocial; - Gerando os eventos, o S1200 de exclusão será gerado para ser liberado ao envio; - Depois da exclusão realizada com sucesso; |
| --- |

![Imagem 5: Marque a liberação da folha para Esocial;](https://ajuda.sankhya.com.br/hc/article_attachments/16147383865751) Marque a liberação da folha para Esocial;

| - MGE **Pessoal>>Avançado>> Liberar o envio da folha ao esocial;** - Gere os eventos e envio o S1200 de inclusão; |
| --- |

![Imagem 6: Após os passos, verifique no portal do esocial, que os valores de plano de saúde estarão conforme a folha.](https://ajuda.sankhya.com.br/hc/article_attachments/16147356623255) Após os passos, verifique no portal do esocial, que os valores de plano de saúde estarão conforme a folha.
