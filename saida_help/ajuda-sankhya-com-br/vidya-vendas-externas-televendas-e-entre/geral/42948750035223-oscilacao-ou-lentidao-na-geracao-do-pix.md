---
id: "42948750035223"
titulo: "Oscilação ou Lentidão na geração do Pix "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948750035223-Oscila%C3%A7%C3%A3o-ou-Lentid%C3%A3o-na-gera%C3%A7%C3%A3o-do-Pix"
trilha: "VIDYA: Vendas externas, televendas e entregas > Geral"
atualizado_em: "2026-08-24T16:51:01Z"
rotulos: ["sync_hc", "vidya", "sync_hash_cc33d3d13435", "vidya_533481"]
---

# Oscilação ou Lentidão na geração do Pix 

## Passo 1: Testar a Geração do Código Pix

1. Acesse o sistema normalmente.
2. Crie um **pedido de teste**.
3. Tente **gerar o código Pix** para esse pedido.
4. Observe se há **lentidão**, erro ou falha na geração do código.

Se o código for gerado normalmente, o problema pode ser pontual ou específico de um pedido. Caso o problema persista, siga para o próximo passo.

---

## Passo 2: Verificar Instabilidade no Banco Responsável

1. Acesse o site: <https://downdetector.com.br>.
2. No campo de busca, digite o nome do banco que está apresentando problema (ex: Itaú, Banco do Brasil, etc.).
3. Verifique se existem **muitas reclamações ou intercorrências** nas últimas horas.

Se o banco estiver com instabilidade, isso pode impactar diretamente a geração do código Pix. Nessa situação, o recomendado é **aguardar a normalização do serviço bancário**.

---

## Passo 3: Verificar o Servidor vidyapay na AWS

1. Acesse o Elastic Beanstalk no AWS.
2. Localize o **servidor vidyapay**.
3. Verifique o status do servidor:

   - Se estiver **RED**, significa que há falha crítica.
4. **Reinicie o servidor** para tentar restaurar a operação normal.

![Imagem 1: Reinicie o servidor para tentar restaurar a operação normal.](https://ajuda.sankhya.com.br/hc/article_attachments/42957221504151)
