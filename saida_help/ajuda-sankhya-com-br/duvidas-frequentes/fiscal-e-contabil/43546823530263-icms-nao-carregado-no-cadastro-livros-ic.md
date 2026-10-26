---
id: "43546823530263"
titulo: "ICMS não carregado no Cadastro Livros ICMS/IPI: como identificar e corrigir"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43546823530263-ICMS-n%C3%A3o-carregado-no-Cadastro-Livros-ICMS-IPI-como-identificar-e-corrigir"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-10-19T19:26:45Z"
rotulos: ["Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# ICMS não carregado no Cadastro Livros ICMS/IPI: como identificar e corrigir

Saiba como proceder quando o valor do ICMS não é apresentado no Cadastro Livro ICMS/IPI.

No “Cadastro Livro ICMS/IPI” (Livros Fiscais > Arquivos), a nota aparece com o valor do ICMS zerado. O valor da nota fica nas colunas Isentas ou Outras

### Principais causas do ICMS não carregado

### Causa

O livro registra o ICMS conforme a configuração da operação e os valores da própria nota. O ICMS fica zerado quando:

- **Na TOP da nota**, o campo “Tipo de ICMS” está como “Sem créd/déb - Isentas” ou “Sem créd/déb - Outras”.
- **No CFOP do item**, o campo “ICMS p/ o Livro Fiscal” está como “Sem créd/déb - Isentas” ou “Sem créd/déb - Outras”. Esse campo vale mais que a configuração da TOP.
- **A própria nota não tem ICMS**, por um destes motivos:
  - a TOP está com “Tem ICMS” desmarcado;
  - a TOP está com “Cálculo de ICMS, IPI, ISS, IBS, CBS e IS” como “Não calcula e não digita”;
  - a empresa está com “Calcula ICMS?” desmarcado (Comercial > Preferências > Empresa).
- **O livro não foi gerado de novo** depois da correção.

### Como corrigir o não carregamento do ICMS

Passos para garantir que o ICMS seja apresentado corretamente no livro fiscal.

Para corrigir a ausência do ICMS no **"Cadastro Livro ICMS/IPI"**, siga o passo a passo:

**(1)**  Na TOP da nota, deixe “Tipo de ICMS” como **“Com créd/déb de imposto”** e confira se “Tem ICMS” está marcado.

**(2)**  Na tela CFOP, deixe “ICMS p/ o Livro Fiscal” como **“Usar da TOP/Empresa”** no CFOP usado nos itens. Mantenha “Sem créd/déb” só quando a operação realmente não tiver crédito ou débito de ICMS.

**(3)**  Se a própria nota foi emitida sem ICMS, corrija a configuração para as próximas notas. Para a nota já emitida, verifique com o responsável fiscal como corrigir o documento, porque o livro só repete o valor da nota.

**(4)**  Em “Geração ICMS/IPI” (Livros Fiscais > Arquivos), gere de novo o período.

**(5)**  Confira o valor no “Cadastro Livro ICMS/IPI”.

**Importante:** a geração usa a configuração da TOP que está gravada em cada nota. Se a correção na TOP criar uma nova versão dela, as notas antigas continuam com a configuração anterior. Já a mudança no CFOP passa a valer na próxima geração.

---

###
