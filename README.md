# 바른정책자금연구소 랜딩페이지

소상공인 정책자금 컨설팅 — YouTube 광고 유입용 단일 페이지 사이트.

## 🎯 프로젝트 정보

- **회사**: 바른정책자금연구소
- **대표**: 강정균
- **연락처**: 1666-0266
- **이메일**: kjgman0711@gmail.com
- **주소**: 인천광역시 연수구 송도동 214 송도비알씨스마트밸리지식산업센터 D동 1603호
- **사업자등록번호**: 292-54-01028

## 🛠 기술 스택

- **HTML** — 순수 HTML (프레임워크 X)
- **Tailwind CSS** — CDN 방식
- **Pretendard** — 한국어 웹 폰트
- **JavaScript (Vanilla)** — 폼 제출, 스크롤 애니메이션, 카운터
- **Zapier Webhook** — 폼 데이터 처리
- **Google Tag Manager** — 광고 전환 추적

## 📁 파일 구조

```
bareun-landing/
├── index.html         메인 랜딩페이지
├── thank-you.html     신청 완료 페이지 (GTM 전환 트리거)
├── images/            이미지 자산
│   ├── 6단체사진.png
│   ├── 넥타이강정균.jpg
│   ├── 대한민국.gif
│   └── case1~6.png    (실사례 카드 사진)
├── .gitignore
└── README.md
```

## 🔌 외부 연동

| 항목 | 설정 |
|------|------|
| Zapier Webhook | `https://hooks.zapier.com/hooks/catch/23898261/urtjt4m/` |
| GTM 컨테이너 | `GTM-PM773BPG` |
| Google Ads 전환 | AW-17521798239 / 4CXXCMrw4robEN_YhaNB |
| 폼 전환 트리거 | `/thank-you` 페이지뷰 |

## 📋 페이지 구성

1. **헤로** — 헤드라인 + CEO 사진 + 라이브 데이터 패널 + 시계 배경
2. **헤로 빠른 폼** — 이름·연락처·사업자유형·연매출·체납 (간소)
3. **어려움 공감** — 3개 카드 (모바일 자동 스와이프)
4. **USP** — 강정균 대표 사진
5. **실사례** — 6개 카드 (네이버 블로그 개별 글 연결)
6. **유튜브** — 강정균 대표 영상 + 채널 CTA
7. **비교표** — 일반대출 vs 정책자금
8. **5년 이자 추이** — 라인 차트 (스크롤 트리거 + 펌핑 애니메이션)
9. **선정 자격** — 3개 카드
10. **절차 3단계**
11. **FAQ** — 6개 질문
12. **3가지 약속** — 상담 무료 / 선수수료 0원 / 1년 관리
13. **본 신청 폼** — 풀버전 (이름·연락처·유형·매출·체납·상호·동의)
14. **푸터**

## 💻 로컬 개발

서버 없이 `index.html` 더블클릭만 하면 브라우저에서 바로 확인 가능. 폼 제출도 정상 작동 (`mode: 'no-cors'`).

## 🚀 배포

현재는 로컬 파일. 배포 옵션:
- **Netlify Drop** — 폴더 드래그 → URL 발급 (무료)
- **Vercel** — 깃허브 연동 자동 배포
- **GitHub Pages** — Public 저장소 필요

## 🔄 작업 흐름 (양쪽 컴퓨터)

### 작업 시작 전
- 윈도우: `git pull`
- 맥북: GitHub Desktop → Fetch origin → Pull

### 작업 끝난 후
- 윈도우: `git add . && git commit -m "내용" && git push`
- 맥북: GitHub Desktop → Commit to main → Push origin

## 📞 문의

작업 관련: kjgman0711@gmail.com
