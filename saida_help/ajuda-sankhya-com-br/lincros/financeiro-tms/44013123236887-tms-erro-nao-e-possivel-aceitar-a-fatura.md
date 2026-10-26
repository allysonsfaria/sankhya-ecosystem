---
id: "44013123236887"
titulo: "[TMS] - Erro 'Não é possível aceitar a fatura X pois há conhecimentos não transportados' ao aceitar faturas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013123236887--TMS-Erro-N%C3%A3o-%C3%A9-poss%C3%ADvel-aceitar-a-fatura-X-pois-h%C3%A1-conhecimentos-n%C3%A3o-transportados-ao-aceitar-faturas"
trilha: "Lincros > TMS > Financeiro - TMS"
atualizado_em: "2026-10-05T19:47:39Z"
rotulos: ["sync_hc", "lincros", "sync_hash_d29239576b38", "lincros_13432965"]
---

# [TMS] - Erro 'Não é possível aceitar a fatura X pois há conhecimentos não transportados' ao aceitar faturas

**Menu**: Financeiro > Faturas

**Objetivo**: Como corrigir a mensagem de erro: "Não é possível aceitar a fatura 'Número da fatura' pois há conhecimentos não transportados" ao aceitar faturas

**Considerações**:

- Possuir faturas para que sejam feitas o aceite;
- Dentro da fatura deve contar pré-conhecimentos com a situação 'Embarcado';

## Exemplo da mensagem ao tentar realizar o aceite da fatura

![Imagem 1: Exemplo da mensagem ao tentar realizar o aceite da fatura](https://ajuda.sankhya.com.br/hc/article_attachments/44013106930583)

Abaixo segue os procedimentos:

1. Acessar a fatura no qual está ocorrendo a mensagem ao aceitar através do menu: Financeiro > Faturas;
2. Acessar a aba 'Conhecimentos Eletrônicos';
3. Verificar se existe algum conhecimento eletrônico que esteja com a situação 'Embarcado', conforme exemplo abaixo:

![Imagem 2: Verificar se existe algum conhecimento eletrônico que esteja com a situação 'Embarcado', conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44013075886999)

4. Verificar se o embarque deste pré-conhecimento está com a situação 'Criado';

5. Verificar se os demais pré-conhecimentos e notas fiscais vinculados ao embarque se estão como ‘Transportada’, após basta recalcular o embarque em questão, clicando no botão 'Recalcular';

![Imagem 3: 5. Verificar se os demais pré-conhecimentos e notas fiscais vinculados ao embarque se estão como ‘Transportada’, após…](https://ajuda.sankhya.com.br/hc/article_attachments/44013076052631)

6. Após, verificar se o mesmo mudou de 'Criado' para 'Transportado';

7. Feito isso, basta aceitar a fatura novamente e verificar que a mesma foi aceita com sucesso;

![Imagem 4: 7. Feito isso, basta aceitar a fatura novamente e verificar que a mesma foi aceita com sucesso;](https://ajuda.sankhya.com.br/hc/article_attachments/44013123897751)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
