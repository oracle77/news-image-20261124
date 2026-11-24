# News facts behind entry.png — Tuesday 24 November 2026
# Researched 2026-11-25 ~08:00 KST via web search; each item
# corroborated by at least two outlets where noted.
# Competition: make.fun news-image-20261124, "Sum up 24 November's
# world news in one image", prize $100 (1st $20), deadline 2026-11-26 09:00 KST.
# NOTE: preparation only — no repo created, nothing submitted.
# API snapshot at research time: 12,275 submissions (2026-11-24 22:49 UTC).

## Hero — Houthi drone attack hits Riyadh's tallest tower (Tue 24 Nov)
- A Houthi drone attack struck a tower in Riyadh's King Abdullah Financial
  District on Tuesday, injuring 11 people (2 Saudis, 2 Indians, 3 Nepalis,
  4 Egyptians), according to Saudi Civil Defence. Witnesses identified the
  building as the 80-storey, 385 m Public Investment Fund (PIF) Tower —
  the capital's tallest skyscraper and HQ of the sovereign wealth fund.
  It is the second strike on the same tower in less than a week (first on
  Thu 19 Nov, damage but no injuries). The Saudi-led coalition called it
  a "terrorist attack"; Arab states condemned it.
  (Al Jazeera, Arab News, WSJ, Dawn, Moneycontrol — all 24 Nov)

## War — Israeli strikes kill 7 in Gaza, incl. Hamas security chief (Tue 24 Nov)
- Israeli airstrikes in Gaza on Tuesday killed seven people including
  Naeem Abu Nahel, director of Hamas' internal security apparatus, and
  two police officers, according to medics and police — despite a
  ceasefire in place since last year. Israeli strikes the previous day
  killed at least three people in Gaza, including a man working for the
  UN Palestinian refugee agency.
  (Just Security Early Edition 24 Nov, Gulf News, Reuters via The Global Eye)

## War — Russian strike kills 2 in Zaporizhzhia (overnight Mon→Tue, confirmed Tue 24 Nov)
- An overnight Russian attack on Zaporizhzhia killed two people and
  wounded 44 others, including four children, striking an apartment
  building, regional governor Mykhailo Semikin said Tuesday. (Naharnet/AP.)
  Note: Just Security's Early Edition gives "another 40 people" wounded —
  the image uses 44 (AP via Naharnet); the "dozens wounded" fact is agreed.
- Same day: Russia said it shot down nearly 700 Ukrainian drones
  overnight across a wide area including the Moscow region and Crimea.
  (Naharnet, 24 Nov)

## Markets — Dow tops 50,000 for the first time; tech gives back Monday's rally (Tue 24 Nov close)
- ⚠️ VERIFIED SESSION CLOSES (consensus of Investopedia, stockmarketwatch,
  CNBC close figures, Swingfolio, VossReport/Altitude recaps):
  Dow 50,018.70 (+0.85%, +423.39) — first close above 50,000;
  S&P 500 7,201.09 (-0.50%, -36.08); Nasdaq 23,733.54 (-1.48%, -356.02).
  Nvidia fell 5.86% to $155.38 after Monday's +31.5% surge; chip stocks
  slid (Micron -11%, AMD -9%); Anthropic fell below its $83 IPO price.
  Conference Board consumer confidence jumped to 103.3 (forecast 92.2).
- ⚠️ Minor variance: Economic Times live blog gives slightly different
  closes (S&P 7,202.45, Nasdaq 23,740.52, Dow 50,028.79). The image uses
  the CNBC/Investopedia consensus above; the direction and the Dow-50k
  milestone are agreed by all sources. Baystreet's figures (-0.6% S&P to
  7,161.28) look like a different snapshot and were NOT used.

## Asia — Hanoi hot-pot eatery gas blast kills 6 (Tue 24 Nov, morning)
- An explosion at a hot pot eatery in Hanoi's Dong Da district at about
  08:00 local Tuesday, suspected to have been caused by a gas leak/cylinder,
  killed six people and injured more than a dozen (10 in intensive care
  per the city release; AP reports "more than 14" hospitalised). The blast
  shattered windows, cracked walls, tore metal shutters off and partly
  brought down the building, damaging nearby houses.
  (AP via Fire Engineering/Manila Times, Reuters via Straits Times,
  Al Jazeera, People — all 24 Nov)

## ALSO strip — Iran: 4 tankers hit mines in Hormuz; rial plunges (Tue 24 Nov)
- Iran's IRGC Navy said four tankers caught fire after striking sea mines
  in the Strait of Hormuz while using "unauthorised" routes; the claims
  have NOT been independently confirmed. UKMTO separately confirmed a
  tanker was struck by an unknown projectile in the strait on 22 Nov.
  The Iranian rial plunged on the black market Tuesday to ~2.82 million
  per US dollar (from ~2.68m Monday) after fresh US sanctions on Iranian
  shadow-banking networks (announced Mon 23 Nov). Iran ruled out US talks
  until seven conditions are met.
  (Al Jazeera live blog, Gulf News, Geo.tv — 24 Nov)

## Verified 7th story — NOT drawn (space)
- Anthropic shares fell below their $83 IPO price on Tuesday, days after
  the 19 Nov debut. (Investopedia headline 24 Nov; VossReport/Altitude
  closing recaps.) Kept out only because the page holds hero + 4 panels
  + 1 ALSO strip.

## Deliberately NOT used
- Jensen Huang / Nvidia +31.5% / Monday market rally: the 1123 hero and
  markets panel — 23 Nov news, excluded by the day rule.
- Ukraine sinking a Russian warship off Libya (23 Nov): 1123 story — the
  24 Nov follow-up (Kyiv/Libya debating legitimacy) is commentary on a
  23 Nov event, not 24 Nov news — excluded.
- US Treasury Iran sanctions (23 Nov, 22 entities + 8 people): 1123's
  7th story — the 24 Nov development (rial plunge) is drawn via the ALSO
  strip instead, as a fresh consequence.
- Trump death-penalty directive / DOJ death sentences: single-source in
  this pass (Just Security Early Edition) — excluded for lack of a second
  corroboration.
- South Korea: Russian aircraft in KADIZ; $375,000 rewards to catch AI
  cheating in the CSAT: single-source in this pass (Just Security) —
  excluded for lack of a second corroboration.
- NATO chief Rutte on Russian nuclear-armed satellite reports: reports
  of reports, no confirmed event on 24 Nov — excluded.
- DRC Ebola responders trapped by fighting: real 24 Nov item (UN News via
  The Global Eye) but single-source in this pass — excluded; would be the
  8th story if space allowed.

---

# 이미지 구성안 (1024×1024, 1123 패턴 재사용 — PIL 코드 렌더링 신문 1면)

심사관이 뉴스 피드 없이 이미지만 보고 판단하므로, 날짜·사건·숫자가
이미지 자체에 모두 읽히게 한다. AI 이미지 모델을 쓰지 않고 PIL로
텍스트를 직접 그려 글자 깨짐을 원천 차단한다 (1118/1123 검증 패턴).

- 마스트헤드: `WORLD NEWS` + `TUESDAY  ·  24 NOVEMBER 2026` (빨간색 날짜줄)
- 히어로 (네이비 패널, 상단 192–474): `MIDDLE EAST  ·  RIYADH`
  "HOUTHI DRONE HITS RIYADH TOWER"
  덱: "11 injured in strike on PIF skyscraper; / 2nd hit in under a week."
  아이콘: 타워 (신규, 단순 도형 — 고층 빌딩 + 창문 격자 + 충격 표시)
- 2행 좌: `WAR  ·  GAZA` — "ISRAELI STRIKES KILL 7 IN GAZA"
  덱: "Hamas security chief among dead despite ceasefire."
- 2행 우: `WAR  ·  UKRAINE` — "RUSSIAN STRIKE KILLS 2 IN ZAPORIZHZHIA"
  덱: "44 wounded, incl. 4 children, in apartment hit."
- 3행 좌: `MARKETS` — "DOW TOPS 50,000 FOR FIRST TIME"
  덱: "Dow +0.9% to 50,018.70; Nasdaq -1.5%, S&P -0.5%."
  (검증된 세션 종료 값만 사용 — Economic Times의 소수점 차이 나는
  종가는 제외하고 CNBC/Investopedia 컨센서스 사용)
- 3행 우: `ASIA  ·  DISASTER` — "HANOI GAS BLAST KILLS 6"
  덱: "Hot-pot eatery explosion; 10+ injured in Dong Da."
- 하단 스트립 (검정): `ALSO: Iran says 4 tankers hit mines in Hormuz; rial plunges`
- 지역·분야 분산: 중동(리야드·가자·호르무즈) / 전쟁(우크라이나) / 시장 / 아시아 재난.
  히어로 1건 + 서브 4건 + ALSO 1건 = 1118/1122/1123과 동일한 6개 스토리 구조.

---

# 제출 요건 체크리스트 (준비 단계에서 확인 — 제출은 사용자 승인 후 별도 단계)

- [ ] 공개 레포 `oracle77/news-image-20261124` — 개시(2026-11-24T00:00:00Z) 이후 생성
      ※ 아직 생성 안 됨 — 사용자 승인 필요 (이 작업에서는 금지)
- [ ] 파일: `main.py`, `entry.png`, `render_image.py`, `NEWS.md`, `LICENSE`(MIT),
      `README.md`(배지 3종) — 이 폴더에 초안 준비됨
- [ ] `entry.png`: PNG, 최대 1 MiB, 1024×1024px — 렌더 후 `ls -l` + `file`로 확인
- [ ] 결정성: `main.py`는 커밋된 `entry.png`를 `/output/entry.png`로 복사만 함
      (네트워크 없음, 표준 라이브러리만) — 2회 실행 sha256 동일 확인 필요
- [ ] 트랜스크립트 번들: 키트 녹화(`kit.tar.gz` → `transcripts.tar.gz`)는
      제출 단계에서 새로 수행 — 이 작업에서는 키트 다운로드·녹화 안 함
- [ ] 제출 명령(참고용 — 이 작업에서는 실행 금지):
      `makefun submit --competition news-image-20261124 --repo-url
       https://github.com/oracle77/news-image-20261124 --commit <sha>
       --title "24 November 2026 in One Image" --bundle <transcripts.tar.gz>
       --keypair <키페어>` — 1123 § 패턴, 실제 값은 제출 시점에 채움
- [ ] 마감: 2026-11-26 09:00 KST (2026-11-26T00:00:00Z) 이전 제출
- [ ] 제출 한도: 하루 10건·통산 20건, 마지막 제출이 최종본 (1123 회차 기준)
- [ ] 검증: 키트 `check` 통과 + 이미지 직접 확인(겹침·잘림 없음) — 제출 전 단계
- [ ] 제출 수 스냅샷: 12,275건 (2026-11-24 22:49 UTC API 조회) — 1123 같은 시점
      8,930건보다 많음. 50곳 입상 가정 시 naive 입상률 ~0.41%, 기대값 ~$0.08 수준
