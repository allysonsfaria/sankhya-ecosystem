---
id: "360052324894"
titulo: "Propriedade 'AjusteApuracao.CODOBSPADRAO' com largura acima do limite: (x > 5)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052324894-Propriedade-AjusteApuracao-CODOBSPADRAO-com-largura-acima-do-limite-x-5"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:29:18Z"
rotulos: ["#criadoroger", "Configuração", "Fiscal", "ICMS", "Impostos", "Preferências", "#AGUARDANDOVALIDAÇÃO", "Limite Excedido para 'AjusteApuracao.CODOBSPADRAO'", "Erro"]
---

# Propriedade 'AjusteApuracao.CODOBSPADRAO' com largura acima do limite: (x > 5)

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18587059984151) MENSAGEM**:

Propriedade 'AjusteApuracao.CODOBSPADRAO' com largura acima do limite: (x > 5).

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18587023651095) CAUSA:**

Ocorre quando ao clicar sobre o botão "Gerar Dif.Alíq.ICMS em Outros Déb/Créd" na tela **Registro de Apuração do ICMS** (Livros Fiscais » Relatórios » Registro de Apuração do ICMS), com o campo "Dif.ICMS na observação, sem afetar Débito/Crédito" marcado, e o parâmetro **Código da Observação para Diferença de ICMS- CODOBSDIFICMS**  tiver informado um código de observação com mais de 5 dígitos.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18587059994775) SOLUÇÃO:**

![Imagem 4: Acesse a tela 'Preferências' (Configurações » Avançado » Preferências) Procure pelo parâmetro: CODOBSDIFICMS](https://ajuda.sankhya.com.br/hc/article_attachments/18587023659159) Acesse a tela 'Preferências' (Configurações » Avançado » Preferências)
Procure pelo parâmetro: **CODOBSDIFICMS**

![Imagem 5: Informe no campo "Inteiro" do parâmetro o código da observação cadastrada na tela Observações para Notas (Comercial »…](https://ajuda.sankhya.com.br/hc/article_attachments/18587060003735) Informe no campo "Inteiro" do parâmetro o código da observação cadastrada na tela **Observações para Notas (Comercial » Arquivo » Cadastros » Observações para Notas)**, onde este código não pode conter mais do que 5 dígitos.

[GIF animado: Imagem 6: Informe no campo "Inteiro" do parâmetro o código da observação cadastrada na tela Observações para Notas (Comercial »…](https://ajuda.sankhya.com.br/hc/article_attachments/360086936894)
