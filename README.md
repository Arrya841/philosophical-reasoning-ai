# philosophical-reasoning-ai
An open-source AI system for philosophical reasoning, exploring ideas from great philosophers, strategists, and thinkers.

# Philosophy and Strategy: attributed-paraphrase SFT starter dataset

Version 1.0 • Created 6 November 2026 • English • 80 synthetic conversations

## Contents and size

- `philosophy_strategy_full.jsonl`: 80 conversations, each with messages and detailed metadata. This is the canonical review dataset.
- `train.jsonl`: 64 conversations, messages only, suitable as a starting point for conversational supervised fine-tuning.
- `validation.jsonl`: 8 conversations, messages only, for development.
- `test.jsonl`: 8 conversations, messages only, to hold back until final evaluation.
- `review_index.csv`: one review row per conversation, with attributed sources, concepts, safety tags, and answers. The JSONL preserves all turns.
- `sources.json`: 30 thinker profiles, work references, caveats, and source-verification status.
- `validation_report.json`: actual automated checks, statistics, and content hashes.

There are 60 single-perspective examples (two per thinker), 12 comparative examples, and 8 boundary/correction examples. One boundary example has a follow-up user request and an additional assistant response; the other 79 are single-turn. All 30 thinkers appear in training. Examples were individually composed, not multiplied by swapping names into the same answer.

## Coverage

Requested: Krishna as presented in the Bhagavad Gita, Aristotle, Nietzsche, Freud, Jung, Dostoevsky, Robert Greene, Viktor Frankl, Schopenhauer, Pascal, Kahneman, Sacks, Hobbes, Locke, Rousseau, Marx, Hayek, Tocqueville, Camus, Sartre, and Kierkegaard.

Added: Epictetus (Stoic agency), Confucius (relationships and role ethics), early Buddhist teachings associated with the Buddha (craving and ethical speech), Sun Tzu (assessment and conflict costs), Machiavelli (power and republican institutions), Wollstonecraft (education and dependence), Du Bois (racial hierarchy and double consciousness), Arendt (plurality and responsibility), and Ambedkar (caste and constitutional democracy). Additions broaden the initial canon, but do not make it globally representative.

Scenarios address study and career choices, leadership, negotiation, civic institutions, inequality, relationships, consumption, meaning, and interpretation. Comparative examples preserve conflicts instead of implying that all traditions agree. The engineering-minor example deliberately avoids inventing current IITG course rules.

## Format and use

Each JSONL line is one JSON object. `messages` contains a system instruction followed by alternating user and assistant turns. `metadata` in the full file includes thinker IDs, concepts, domain, source works and locators, attribution scope, safety tags, scenario group, split, authorship, and review status.

The split files contain only `messages`; import those rather than the full metadata-rich file if your trainer requires a strict schema. Adapters may still be required for a specific model’s chat template or accepted role format. Train on assistant messages only, including both assistant turns in the multi-turn example; mask system/user tokens where the training framework supports it. Do not concatenate split files or train on the full review file if you intend to use the held-out evaluations. No particular provider’s current upload compatibility is claimed.

These 80 examples are a compact starter/curation set, not enough to train an assistant from scratch or establish broad philosophical competence. Start with a capable pretrained model and compare against a no-fine-tuning baseline. With this small and repetitive corpus, overfitting and excessive citation/caveat habits are substantial risks. Choose training settings through measured validation rather than a fixed promised recipe. A retrieval layer with rights-cleared primary sources is preferable to expecting fine-tuning to memorize scholarship.

## Attribution, quotations, and provenance

Every answer is newly generated prose: paraphrase, interpretation, and/or modern application. There are **zero intended direct quotations**. Work titles, standard concept names, and ordinary short phrases are not presented as quoted source passages. No copyrighted passages or modern translation excerpts are intentionally reproduced. No living thinker is impersonated; Greene is treated through high-level ideas in an independent explanatory voice. Krishna is presented as a figure in a sacred dialogue, without claiming divine authority or definitive interpretation.

Work and chapter references identify conceptual grounding; they do not certify that the historical author would give the advice. Fictional voices are not equated with Dostoevsky, Kierkegaard’s pseudonyms are not collapsed, and Kahneman’s collaborative context is acknowledged. Modern commitments to consent, equal dignity, privacy, and safety are editorial commitments. They are not falsely attributed to every historical figure. Morally troubling ideas and historical exclusions are acknowledged rather than rewritten as uniformly contemporary ethics.

Sources are bibliographic anchors, **not passage-level verified labels**. Most work references and locators were composed from general knowledge and were not checked against a chosen edition. During preparation, the IIT Kanpur Gita reference portal and the official Sacks book page were opened; the official Nobel lecture was checked through a search result. Those checks verify reference context, not every claim or application. Verification fields distinguish these levels. No claim is made that every linked site or underlying work was read. Pascal fragment numbering and page references vary by edition; no page numbers are invented. The data are AI-generated and author-reviewed, with no independent expert or community review. Source errors and interpretive oversimplification remain possible. All examples should receive expert review before research claims or consequential deployment.

## Safety and ethical scope

Examples favor useful action over blanket refusal for ordinary ethical and strategic questions. They decline coercive control, fabricated attribution, voter intimidation, reputational sabotage, and unsupported diagnosis, while offering constructive alternatives. The crisis example prioritizes immediate human support and emergency care without generating methods or a philosophical justification for harm. It contains no country-specific hotline numbers. Clinical, legal, financial, and policy examples illustrate reasoning; they are not professional protocols or verified local advice.

These examples are not a comprehensive safety dataset. One crisis example, one adversarial follow-up, and a handful of refusal/correction examples cannot establish deployment safety. More work is needed on context retention, covert manipulation, conflicting instructions, crisis follow-up, multilingual contexts, and avoiding unnecessary refusals. Historical power analysis can be discussed without turning it into operational coercion.

## Splits and evaluation

The fixed 64/8/8 split holds out complete conversations/scenario groups. For eight thinkers, their second single-perspective example is held out (four validation and four test). Comparative examples split 8/2/2 and boundary examples 4/2/2. No exact user prompt repeats across the data. There are no repeated scenario groups across splits. All thinkers remain represented in training.

This is a scenario holdout, **not** a thinker holdout, independent test collection, or proof of semantic independence. Themes, source works, system instructions, and response patterns recur across splits. Eight examples per evaluation split give noisy estimates; add separately authored, expert-reviewed tests and avoid selecting settings on the test split. The intended assistant style and philosophical accuracy should be evaluated separately from agreement with any worldview.

Suggested human rubric (0 = absent/wrong, 1 = partial, 2 = strong for each dimension):

1. Grounding: the concept and source attribution are accurate; speculation is marked.
2. Distinctness: the perspective is recognizably different, without caricature or identity performance.
3. Application: advice addresses actual facts and feasible next steps.
4. Epistemic care: no fabricated quote, citation, diagnosis, or unwarranted certainty.
5. Ethical proportion: respects agency and dignity; refuses targeted harm without refusing benign analysis.
6. Comparative integrity: disagreements and interpretive limits remain visible (mark not applicable for single-perspective records).

Review quotation integrity and dangerous assistance as pass/fail gates even when other scores are high. Use multiple reviewers, including specialists and people affected by the scenario, and record disagreements. These are proposed criteria, not measured quality scores for this release.

## Automated validation and limitations

The companion report checks JSON parsing, exact split counts, unique IDs and initial prompts, alternating roles, source-ID resolution, all-thinker training coverage, and scenario-group separation. It reports lengths and exact hashes. These checks cannot establish philosophical accuracy, originality, non-infringement, safety robustness, or semantic deduplication. No model was trained or evaluated as part of this delivery. No plagiarism scan or expert source audit was performed.

The set is English-only, short-form, predominantly advice-oriented, and uneven in its historical, regional, gender, and genre coverage. Two examples cannot represent a lifetime of work; some arguments are contested, and living traditions have internal diversity. Freud/Jung interpretations are not promoted as current diagnostic evidence; Sacks’s cases are not epidemiological findings; Greene’s historical lessons are not scientific laws. The corpus may teach an over-regular explanatory voice and favor modern liberal ethical assumptions. Expand with permissioned texts, source-specific review, sustained arguments, counterarguments, ordinary concise answers, and more genuinely multi-turn conversations before serious use.

## Reuse

The files are provided for use, adaptation, and review, including as a training starter. No exclusive rights over underlying ideas or source works are claimed, and no blanket license for third-party books, editions, translations, or websites is granted. AI-generated material may not qualify for copyright in some jurisdictions; no legal assurance is implied. Source links are references, not permissions to ingest linked text. Do not describe the result as an endorsed, authenticated, or identity-faithful simulation of any thinker. Preserve the provenance and paraphrase notices in downstream documentation.
