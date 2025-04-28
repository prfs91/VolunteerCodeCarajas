<!--

docs/
├── guides/                          	    # Guias práticos agrupados por domínio
│   ├── workflow/                    	    # Fluxos de trabalho e regras
│   │   ├── commit-conventions.md    	    # Convenção de commits
│   │   ├── branching-strategy.md    	    # Estratégia de branches
│   │   └── pull-request-process.md  	    # Processo de PRs

# Convenção de commits

-->

# 🧭 **Guia de Commits Bem-Organizados: VolunteerCodeCarajas**

## 🚀 Por que seguir este guia?

Manter um padrão nos commits:

* Facilita o entendimento do histórico de alterações.
* Ajuda outras pessoas (e você mesma no futuro) a entender  **o que foi feito, onde e por quê**.
* Melhora a organização, a produtividade da equipe e a revisão de código.
* É essencial para projetos colaborativos, com controle de versões, releases, revisões de código e auditoria.

---

## 📝 **1. Estrutura de um Commit**

Um commit pode conter duas partes:

### ✅ **Título** (obrigatório)

* Deve ser curto, direto e descrever a ação principal.
* Máximo recomendado: **50 caracteres**.

  > ⚠️ **Use o título para registrar a ação principal.**
  
  > 📌 **Formato do TÍTULO**

  > ```bash
  > emoji tipo (módulo_ou_pasta): ação_ou_resumo_da_mudança
  > ```

**Exemplo:**
```bash
✨ feat (associados): implementar filtro de associados ativos
```

### 💬 **Descrição** (opcional)

Use para explicar detalhes adicionais:

* Por que a mudança foi feita.
* Como foi implementada.
* Explicações técnicas.
* Pendências ou próximos passos.

**Exemplo:**
```bash
git commit -m "✨ feat (associados): implementar filtro de associados ativos" -m "Filtro por status no admin. Falta adicionar ordenação por data de cadastro."
```
💡 O primeiro `-m` é o título. O segundo (ou mais) adiciona o corpo da mensagem.

---

## 📦 2. Tabela de Emojis

| Emoji | Tipo        | Quando Usar | Exemplo de Commit |
| ----- | ----------- | ----------- | --------------- |
| ✨    | `feat`      | Nova funcionalidade | `✨ feat: adicionar página de cadastro de usuários` |
| 🐛    | `fix`       | Correção de bug | `🐛 fix (api): corrigir resposta HTTP 500 no cadastro` |
| 📦    | `build`     | Mudanças em dependências ou ferramentas de build | `📦 build: atualizar dependências do projeto` |
| 📚    | `docs`      | Alterações em documentação | `📚 docs: criar guia de configuração do projeto` |
| ♻️    | `refactor`  | Refatoração sem mudar funcionalidades | `♻️ refactor: melhorar validação de CPF` |
| 🎨    | `style`     | Estilo (espaços, identação, etc — sem alterar lógica) | `🎨 style: corrigir alinhamento dos botões` |
| 🚀    | `deploy`    | Quando o código for para produção | `🚀 deploy: nova versão v1.2.3 em produção` |
| ✅    | `test`      | Adição/correção de testes | `✅ test: adicionar testes unitários para cadastro` |
| 🔧    | `chore`     | Tarefas de manutenção sem impacto direto no código | `🔧 chore: atualizar versão do Node no package.json` |
| 🚧    | `WIP`       | Trabalho em progresso | `🚧 WIP: ajustes no fluxo de recuperação de senha` |
| 🔥    | `remove`    | Remoção de código ou arquivos desnecessários | `🔥 remove: excluir arquivos não utilizados da pasta assets` |
| ➕    | `add`       | Adição de arquivos ou códigos simples | `➕ add: adicionar script de inicialização` |
| ➖    | `delete`    | Exclusão intencional de funcionalidades/códigos | `➖ delete: remover campo telefone do formulário` |
| 💄    | `ui`        | Mudanças visuais na interface | `💄 ui: mudar cores dos alertas para o padrão institucional` |
| 🗃️    | `structure` | Organização ou reestruturação de pastas e arquivos | `🗃️ structure: mover páginas para pasta admin/` |
| 📈    | `perf`      | Melhorias de performance | `📈 perf: otimizar consulta de associados no banco`    |
| ⬆️    | `upgrade`   | Atualização de dependência ou versão específica | `⬆️ upgrade: atualizar Django para 4.2` |
| ⬇️    | `downgrade` | Reversão de versão por instabilidade | `⬇️ downgrade: voltar React para 17` |
| 🐳    | `docker`    | Alterações relacionadas a containers ou Dockerfiles  | `🐳 docker: configurar volumes no docker-compose` |
| 🛠️    | `config`    | Configurações de ferramentas, linter, CI/CD etc. | `🛠️ config: adicionar suporte a imports absolutos` |

---

## 🔥 **3. Commits Atômicos**

- **Cada commit deve alterar apenas UMA funcionalidade** ou UM propósito principal.
- Commits atômicos facilitam revert, cherry-pick e entender o histórico.

**Errado** (muitos assuntos no mesmo commit):

```bash
✨ feat: adicionar cadastro + corrigir bug no login + refatorar form
```

**Certo** (commits separados):

```bash
✨ feat (cadastro): adicionar novo campo de data de nascimento
```

```bash
🐛 fix (login): corrigir erro de autenticação de senha inválida
```

```bash
♻️ refactor (form): melhorar validação de inputs
```

---

## 🔄 **4. Commits de Merge**

Quando fizer merge manual:

- Escreva o commit de merge claramente.
- Evite deixar apenas o padrão automático do Git.

**Exemplo de commit de merge:**

```bash
🔀 merge: integrar branch feature/relatorios no develop
```

---

## 🛠️ **5. Commits de Hotfix**

Se corrigir algo crítico direto na produção (hotfix):

Use `fix` + anotação clara de hotfix.

**Exemplo:**

```bash
🐛 fix (prod): corrigir erro crítico de login em produção
```

---

## ↩️ **6. Commits de Revert**

Para reverter uma mudança:

Use o comando `git revert` para manter o histórico limpo.

Padronize o commit de reversão:

**Exemplo:**

```bash
⏪ revert (login): desfazer validação extra de email duplicado
```

---

## 🌱 **7. Padrão de Nome para Branches**

Nomear branches de forma clara e sem espaços:

```bash
tipo/descricao-breve
```

Exemplos:

```bash
feat/cadastro-associados
```

```bash
fix/corrigir-validacao-login
```

```bash
refactor/melhorar-performance-filtros
```

```bash
docs/adicionar-tutorial-setup
```

```bash
chore/atualizar-dependencias
```

---

## ✅ **8. Checklist Antes de Commits**

Antes de commitar, pergunte-se:

- [ ] Meu commit é atômico?
- [ ] O título está claro, objetivo e padronizado?
- [ ] Usei o emoji correto?
- [ ] (Se necessário) Expliquei o que falta na descrição?
- [ ] Está relacionado à branch atual?
- [ ] Está documentado para que qualquer pessoa entenda?

---

## 📌 **9. Exemplo Completo: Commit Ideal**

```bash
git commit -m "✨ feat (associados): permitir cadastro em lote" -m "Utiliza formulário de múltiplos uploads. Falta revisar validação de campos obrigatórios."
```

---

## 🏁 **10. Dica Final**

Para commits mais organizados e padronizados, é recomendado usar o **editor de commits** do Git em vez de passar tudo pelo `-m`.
Assim, você consegue separar corretamente o **título** e o **corpo** da mensagem.

Abra o editor do Git com:

```bash
git commit
```

Quando o editor abrir (padrão é o Vim, ou VS Code se estiver configurado), a estrutura que você deve seguir é:

1. A **primeira linha** deve conter o **Título do Commit**.
   
    → Essa linha é curta e objetiva (recomenda-se até 50 caracteres).

2. Depois da primeira linha, **deixe uma linha em branco**.
   
    → Essa separação é obrigatória para o Git interpretar corretamente.

3. Nas próximas linhas, você pode escrever a **Descrição Detalhada** (opcional), explicando o que foi feito, por quê, pontos pendentes, etc.

🧩 **Exemplo de estrutura no editor:**

```bash
✨ feat (cadastro): validar CPF antes de enviar formulário

- Utilizado regex simples para validação
- Futuro: aplicar validação oficial via Receita Federal
```

✔️ **Notas importantes:**

* Nunca escreva a descrição logo abaixo do título sem pular uma linha.
* Use o título para resumir a ação principal.
* Use a descrição para explicar detalhes técnicos, justificativas ou próximos passos, se necessário.
* Salve e feche o editor para concluir o commit (`:wq` no Vim, ou `CTRL+S` e fechar o editor gráfico).

---

> ⚠️ **Aviso Importante:**
> 
> Esta documentação está em fase de desenvolvimento. 
> Algumas seções podem estar incompletas ou temporariamente indisponíveis.
> Atualizações estão sendo realizadas de forma contínua para aprimorar o conteúdo.

---

<p align="center">
  📚 Este documento integra a documentação oficial do projeto <strong>VolunteerCodeCarajas</strong>.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/robertaferreira91/" target="_blank"><img width="25" height="25" title="LinkedIn" src="https://img.icons8.com/?size=100&id=xuvGCOXi8Wyg&format=png&color=000000"/></a>
  <a href="mailto:pamellaferreira.si@gmail.com" target="_blank"><img width="25" height="25" title="Gmail" src="https://img.icons8.com/?size=100&id=P7UIlhbpWzZm&format=png&color=000000"/></a>
  <a href="https://wa.me/5594992797521?text=Ol%C3%A1%21%20Encontrei%20seu%20contato%20atrav%C3%A9s%20do%20GitHub%20e%20gostaria%20de%20conversar%20com%20voc%C3%AA.%20Podemos%20falar%20um%20pouquinho%3F" target="_blank"><img width="25" height="25" title="WhatsApp" src="https://img.icons8.com/?size=100&id=16713&format=png&color=000000"/></a>
  <a href="https://github.com/prfs91" target="_blank"><img width="25" height="25" title="GitHub" src="https://img.icons8.com/?size=100&id=bVGqATNwfhYq&format=png&color=000000"/></a><br>
  <strong>🔖 Licença:</strong> MIT License <br>
  © 2025 - Roberta Ferreira
</p>

---

<p align="right">
  <strong>📅 Última atualização:</strong> 28/04/2025
</p>
