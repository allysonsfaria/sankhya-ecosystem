---
id: "39368651697559"
titulo: "Sistema não está calculando IBS/CBS nas notas de serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39368651697559-Sistema-n%C3%A3o-est%C3%A1-calculando-IBS-CBS-nas-notas-de-servi%C3%A7o"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Dúvidas Frequentes"
atualizado_em: "2026-09-29T12:06:09Z"
rotulos: ["Configuração", "Impostos", "TOP", "NFS-e", "Reforma Tributária", "Artigo criado KCS", "Alíquotas de CBS", "Alíquotas de IBS", "Fiscal/Contábil - KCS"]
---

# Sistema não está calculando IBS/CBS nas notas de serviço

**MENSAGEM**

O sistema não está calculando o Imposto sobre Bens e Serviços nas Notas Fiscais de Serviço (NFS-e), mesmo com as configurações aparentemente corretas.

**SITUAÇÃO**

Ao emitir uma **"Nota Fiscal de Serviço (NFS-e)"**, o usuário verifica que o **"IBS" e "CBS"** não está sendo calculado, mesmo que:

- O **"Tipo de Operação" (TOP)** esteja marcado para calcular o IBS;
- O serviço possua o **"Código NBS"** informado;
- As **"Alíquota do IBS/CBS"** esteja cadastrada para o NBS;

**SOLUÇÃO**

Para resolver o problema do não cálculo do IBS nas notas de serviço, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Configurações Fiscal Tipos de Operação) e localize o TOP utilizado na emissão da NFS-e.

**(2)** Na aba **"Impostos"**, verifique se as marcações para **"Calcular IBS"** e **"Calcular CBS"** estão habilitadas. Importante: o sistema Sankhya exige que ambos os impostos (IBS e CBS) estejam marcados simultaneamente. Não é possível calcular apenas o IBS sem o CBS devido a uma exigência técnica da Reforma Tributária.

**(3)** Verifique o campo **"Finalidade de Operação"** configurado no TOP e anote o código.

**(4)** Acesse a telas **"Alíquota de IBS" e "Alíquota de CBS"** e localize as alíquotas cadastradas.

**(5)** Verifique se o campo **"Finalidade de Operação"** nas alíquotas de IBS e CBS está configurado com o mesmo código definido no TOP. Caso esteja diferente, ajuste para que corresponda ao TOP utilizado.

**(6)** Confirme que o **"Código NBS"** está informado no cadastro do serviço ou usa o valor zero(0).

**(7)** Após realizar os ajustes necessários, redigite os itens da nota fiscal ou gere uma nova nota para que o sistema recalcule os impostos com as configurações corretas.

**(8)** Valide se os valores de **"IBS"** e **"CBS"** estão sendo calculados e apresentados corretamente na nota fiscal.

**CAUSA**

O problema ocorre devido à incompatibilidade entre as configurações do **"Tipo de Operação" (TOP)** e das **"Alíquotas de IBS e CBS"**. As principais causas identificadas são:

- **Divergência na "Finalidade de Operação":** quando o código da finalidade cadastrado nas alíquotas de IBS e CBS não corresponde ao código configurado no TOP utilizado na emissão da nota;
- **Falta de marcação simultânea de IBS e CBS:** o sistema Sankhya exige que ambos os impostos estejam habilitados no TOP. Não é possível calcular apenas o IBS sem o CBS, conforme exigência técnica da Reforma Tributária;
- **Notas originadas antes das configurações:** em casos de devolução ou referência a notas anteriores, se a nota de origem foi lançada antes da configuração das alíquotas de IBS e CBS, a nota derivada não calculará os impostos automaticamente.
- **Divergência no NBS:** quando o código de NBS cadastrado nas alíquotas de IBS e CBS não corresponde ao código configurado no serviço ou está usando o campo de NCM;
