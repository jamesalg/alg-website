# Setup Walkthrough — GitHub + Cloudflare Pages

This is the one-time setup. After this, every iteration is just `git push` from Manus.

**Time required:** ~15 minutes total. Mostly clicking.

---

## Part A — Create the GitHub repository (5 minutes)

You will create the repository through the GitHub web interface, then drag-and-drop the foundation files into it.

### A.1 Create the empty repo

1. Go to **https://github.com/new** (you must be logged in as `jamesalg`)
2. Fill in:
   - **Repository name:** `alg-website`
   - **Description:** `Archipelago Lighting Group corporate website. Astro + Cloudflare Pages.`
   - **Visibility:** **Private** (this is your company website source code; do not make it public)
   - **Initialize this repository with:** UNCHECK "Add a README file" (we have our own). UNCHECK ".gitignore" and "license" too.
3. Click **Create repository**

You'll see an empty repo page with setup instructions. Ignore those instructions; we have a different path.

### A.2 Upload the foundation files

GitHub's web UI lets you drag-and-drop folders. We'll use that.

1. On the empty repo page, find the link that says **"uploading an existing file"** (it's in the quick-setup section, lower down). Click it.

   If you can't find it, go to: `https://github.com/jamesalg/alg-website/upload/main`

2. You'll see a drag-and-drop area saying "Drag files here to add them to your repository".

3. Open the foundation zip I'm sending you (`alg-website-v2.0.0-foundation.zip`). Extract it to a folder on your desktop. You'll see a folder named `alg-website` with all the contents.

4. **OPEN that `alg-website` folder, select ALL files and folders inside it (Cmd+A on Mac), and drag them onto the GitHub upload area.** Important: drag the CONTENTS of `alg-website/`, not the folder itself.

   GitHub will start uploading. With ~70 files including 23 images (~99MB total in `public/`), this might take 30-60 seconds depending on your connection.

5. Once all files show in the file list, scroll down. You'll see a **Commit changes** section.
   - Commit message: `v2.0.0 — Foundation: Astro skeleton, canonical components, playbook, 23 production assets`
   - Description: leave blank or paste: `Foundation commit. Replaces prior platform. See docs/ALG_Build_Playbook_v2.0.md.`
   - Select: **"Commit directly to the `main` branch"**

6. Click **Commit changes**.

You should now see the repository populated. The README will render automatically on the repo home page.

### A.3 Add Manus and (later) Claude as collaborators

1. Go to your repo → **Settings** (top tab) → **Collaborators** (left sidebar)
2. Under "Manage access" click **Add people**
3. Search for Manus's GitHub account (you'll need their handle — ask Manus what it is) and invite as a **Collaborator** with Write access

Manus does NOT need admin access. Just write. They'll be able to push branches and open PRs but not delete the repo or change settings.

### A.4 Create the staging branch protection rule

This enforces that nothing reaches `main` without passing CI.

1. Repo → **Settings** → **Branches** (left sidebar)
2. Click **Add branch protection rule**
3. Branch name pattern: `main`
4. Check these:
   - ✅ Require a pull request before merging
   - ✅ Require approvals (1)
   - ✅ Require status checks to pass before merging
     - In the search box that appears, type `build-and-verify` and select it
   - ✅ Require branches to be up to date before merging
5. Click **Create**

Now `main` is protected. Manus cannot push directly to `main`; everything goes through a PR with green CI.

---

## Part B — Connect Cloudflare Pages (5 minutes)

### B.1 Create the Pages project

1. Go to **https://dash.cloudflare.com** (you should already be logged in)
2. Left sidebar → **Workers & Pages**
3. Click **Create application** → **Pages** tab → **Connect to Git**

### B.2 Authorize GitHub

1. Click **Connect GitHub**
2. A popup opens asking you to authorize Cloudflare to access GitHub
3. Choose **Only select repositories** (more secure than "all repos")
4. Select `alg-website` from your repo list
5. Click **Install & Authorize**

You're now back on the Cloudflare project setup page, with `alg-website` available.

### B.3 Configure the build

1. Select repository: `jamesalg/alg-website`
2. Click **Begin setup**
3. Project settings:
   - **Project name:** `alg-website` (lowercase; this becomes part of the preview URL)
   - **Production branch:** `main`
4. Build settings:
   - **Framework preset:** select **Astro** from the dropdown (Cloudflare auto-fills the rest)
   - Should auto-fill:
     - Build command: `npm run build`
     - Build output directory: `dist`
     - Root directory: `/` (leave blank)
   - **Environment variables:** none needed
5. Click **Save and Deploy**

Cloudflare will start the first build. This takes ~1-2 minutes.

### B.4 First deploy

Watch the build log. You should see:
```
✓ Cloning repository
✓ Installing dependencies (npm install)
✓ Building site (npm run build)
✓ Verification (npm run verify)
✓ Deploying to Cloudflare Pages
```

When it finishes:
- The default URL `alg-website.pages.dev` (or `alg-website-xxx.pages.dev` if Cloudflare appended a suffix) goes live
- The placeholder homepage will render with the brand-mark test text

### B.5 Confirm the staging domain

You already added `staging.archipelagolighting.com` → `alg-website.pages.dev` at GoDaddy. Now we register that custom domain on Cloudflare's side.

1. In your Cloudflare Pages project → **Custom domains** tab
2. Click **Set up a custom domain**
3. Enter: `staging.archipelagolighting.com`
4. Click **Continue**
5. Cloudflare will verify the CNAME (which already exists at GoDaddy from earlier today). Should show ✓ in 1-5 minutes.
6. Once verified, `staging.archipelagolighting.com` serves the placeholder homepage.

If Cloudflare reports the project name doesn't match `alg-website` (it might assign a randomized suffix like `alg-website-r3k`), tell Claude — we'll update the GoDaddy CNAME to match. Quick fix.

---

## Part C — Confirm everything is wired (2 minutes)

After all of the above, you should be able to verify:

1. **GitHub repo:** `https://github.com/jamesalg/alg-website` shows all the files
2. **First Cloudflare deploy succeeded:** the build log says ✓ on every step
3. **Default Cloudflare URL works:** visit `alg-website.pages.dev` — sees the placeholder homepage with the brand-mark test
4. **Staging domain works:** visit `https://staging.archipelagolighting.com` — same placeholder homepage
5. **CI is configured:** GitHub repo → Actions tab shows the Build & Verify workflow has run on the foundation commit and is green ✓

If all 5 are green, the foundation is live. Tell me, and I send the v2.1.0 prompt to Manus.

If anything is red or missing, paste the error and I'll diagnose.

---

## Part D — What happens next

Once Parts A, B, and C are confirmed, the iteration cycle is:

1. **You:** "Foundation confirmed. Send Manus the homepage prompt."
2. **Me (Claude):** I send Manus the v2.1.0 prompt (already written, in `docs/Manus_Prompt_v2_1_0_Homepage.md`)
3. **Manus:** creates branch `iter/v2.1.0-homepage`, commits, pushes, opens PR
4. **CI:** runs automatically on the PR. Green or red status appears.
5. **Cloudflare:** builds the branch automatically. Posts preview URL on the PR.
6. **You + me:** open the preview URL, audit visually
7. **If pass:** I approve PR, you click merge → staging updates automatically
8. **If fail:** I write correction prompt → Manus pushes new commit → loop step 4

That's the loop. After homepage lands, distributor page is next, then collection pages, then PDPs. Each iteration is small and verifiable.

---

## Tools you'll use day to day

- **GitHub** — `https://github.com/jamesalg/alg-website` — to see PRs, click "merge", read commit history. Mostly read-only for you.
- **Cloudflare dashboard** — for build logs and deploy history if anything looks off
- **Browser** — to audit `staging.archipelagolighting.com` and PR preview URLs
- **This chat** — where I write prompts, audit Manus output, and you give approve/reject signals

Email and slack-style messages to Manus happen the way they did this week (you have an active Manus session). The only thing that changes is Manus pushes to GitHub instead of saving "checkpoints" on its own platform.
