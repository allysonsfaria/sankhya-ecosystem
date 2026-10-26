---
id: "44013428390807"
titulo: "[TMS] ICMS não está somando ao total, mesmo com todos os componentes necessários."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013428390807--TMS-ICMS-n%C3%A3o-est%C3%A1-somando-ao-total-mesmo-com-todos-os-componentes-necess%C3%A1rios"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:57:06Z"
rotulos: ["sync_hc", "lincros", "lincros_13432537", "sync_hash_5c4c08317515"]
---

# [TMS] ICMS não está somando ao total, mesmo com todos os componentes necessários.

**Menu:** Configurações Gerais > Configurações da Empresa > Taxas > Taxas Estaduais

**Objetivo:** Apresentar um ponto de análise, para quando o ICMS não está sendo calculado ao valor “calculado” do transporte.

**Considerações:** Em alguns Pré-conhecimentos, embarques, entre outros. Temos o valor calculado sendo apresentado, porém, o ICMS não está somado.

![Imagem 1: Considerações: Em alguns Pré-conhecimentos, embarques, entre outros. Temos o valor calculado sendo apresentado, porém,…](https://ajuda.sankhya.com.br/hc/article_attachments/44013414160535)

Ao validar na tabela, os componentes vão estar com Flag de ICMS marcada, no cadastro da transportadora, também estará com as flags de ICMS marcadas.

Analisando as taxas estaduais, teremos os valores das alíquotas, então o que pode estar ocorrendo?

No cadastro da Taxa temos algumas Flags dente estas “Calcula ICMS CIF” e “Calcula ICMS FOB”.

Observe se ambas estão assinaladas caso não, valide no Pré-Conhecimento qual a forma de negociação.

Exemplo: No Pré-Conhecimento está FOB, porém na taxa está marcado apenas CIF, logo o sistema não irá calcular o ICMS para este Pré-Conhecimento.

![Imagem 2: Exemplo: No Pré-Conhecimento está FOB, porém na taxa está marcado apenas CIF, logo o sistema não irá calcular o ICMS…](https://ajuda.sankhya.com.br/hc/article_attachments/44013405678487)

Após assinalar ambas as Flags, salve a alteração e recalcule o Pré-Conhecimento.

![Imagem 3: Após assinalar ambas as Flags, salve a alteração e recalcule o Pré-Conhecimento.](https://ajuda.sankhya.com.br/hc/article_attachments/44013441465623)

**Conclusão:** Com o processo devidamente realizado, o valor de ICMS, já deverá estar sendo apresentado e somado ao total calculado.
