---
id: "27379013106071"
titulo: "Veja como deduzir o FCP da base de PIS/COFINS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27379013106071-Veja-como-deduzir-o-FCP-da-base-de-PIS-COFINS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:39:42Z"
rotulos: ["Configuração", "COFINS", "PIS", "ICMS", "Impostos", "Preferências", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Veja como deduzir o FCP da base de PIS/COFINS"]
---

# Veja como deduzir o FCP da base de PIS/COFINS

Para que o sistema realize o cálculo conforme o esperado, siga as orientações a seguir:

**(1)** Acesse a tela **"Preferências"** e verifique se o parâmetro ''**REDICMSBCPISCOF''** deve estar habilitado. 

**(1)** Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa), na aba **"Propriedades"**, realize as seguintes configurações:

- **Deduzir valor do ICMS na BC do PIS e COFINS?:** Configurado por TOP

**OBSERVAÇÃO:** Esse campo somente será exibido caso o parâmetro acima esteja ativado.

- **Deduzir valor de FCP e FCP ST na BC do PIS e COFINS?:** configurado por TOP

**(1)** Nas respectivas TOPs:

- **Deduzir valor do ICMS na BC do PIS e COFINS?:** selecionado
- **Deduzir valor de FCP na BC do PIS e COFINS?:** ambos

**OBSERVAÇÃO:** Atualmente, o sistema **não** está apto a realizar tal dedução **para notas de Terceiros** (T - Terceiros). Dessa forma, a dedução ocorre apenas para notas de emissão própria (N - Normal | C - Complementar | A - Ajuste | D - Devolução).
