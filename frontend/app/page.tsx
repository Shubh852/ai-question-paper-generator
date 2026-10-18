'use client';

import React, { useState, useEffect } from 'react';
import Wizard from '../components/Wizard';
import SavedPapersDashboard from '../components/SavedPapersDashboard';
import TeacherAuthModal, { TeacherUser } from '../components/TeacherAuthModal';
import AiCopyCheckerModal from '../components/AiCopyCheckerModal';
import { 
  Sparkles, 
  FileText, 
  GraduationCap, 
  Cpu, 
  Bookmark, 
  UserCheck, 
  LogOut, 
  School,
  ShieldCheck,
  CheckCircle2,
  Layers,
  FileCheck,
  Zap,
  ArrowRight
} from 'lucide-react';

export default function Home() {
  const [activeTab, setActiveTab] = useState<'create' | 'saved'>('create');
  const [loadedExam, setLoadedExam] = useState<any>(null);
  const [teacherUser, setTeacherUser] = useState<TeacherUser | null>(null);
  const [teacherPaperCount, setTeacherPaperCount] = useState<number | null>(null);
  const [isAuthLoaded, setIsAuthLoaded] = useState(false);
  const [isCopyCheckerOpen, setIsCopyCheckerOpen] = useState(false);

  useEffect(() => {
    try {
      const savedAuth = localStorage.getItem('cbse_auth_teacher');
      if (savedAuth) {
        setTeacherUser(JSON.parse(savedAuth));
      }
    } catch {
      // Ignore parse error
    } finally {
      setIsAuthLoaded(true);
    }
  }, []);

  // Fetch teacher stats (papers count) from Supabase / SQLite
  useEffect(() => {
    if (teacherUser?.whatsapp || teacherUser?.email || teacherUser?.id) {
      const id = teacherUser.whatsapp || teacherUser.email || teacherUser.id;
      fetch(`/api/v1/teacher/stats?identifier=${encodeURIComponent(id)}`)
        .then((res) => (res.ok ? res.json() : null))
        .then((data) => {
          if (data && typeof data.total_papers_created === 'number') {
            setTeacherPaperCount(data.total_papers_created);
          }
        })
        .catch(() => {});
    }
  }, [teacherUser, activeTab]);

  const handleLogout = () => {
    if (confirm('Are you sure you want to log out of this educator profile?')) {
      const lastId = teacherUser?.whatsapp || teacherUser?.email;
      if (lastId) {
        localStorage.setItem('cbse_last_identifier', lastId);
      }
      localStorage.setItem('cbse_has_registered', 'true');
      localStorage.removeItem('cbse_auth_teacher');
      setTeacherUser(null);
      setTeacherPaperCount(null);
      setActiveTab('create');
    }
  };

  const handleLoadExamToPreview = async (examId: string) => {
    try {
      const res = await fetch(`/api/v1/saved-exams/${examId}`);
      if (res.ok) {
        const data = await res.json();
        setLoadedExam(data);
        setActiveTab('create');
      } else {
        alert('Could not load saved paper.');
      }
    } catch (e: any) {
      alert(`Error loading paper: ${e.message}`);
    }
  };

  // 1. DEDICATED TEACHER PORTAL GATE (Shown before login)
  if (isAuthLoaded && !teacherUser) {
    return (
      <main className="min-h-screen bg-gradient-to-b from-slate-900 via-indigo-950 to-slate-900 text-white flex flex-col justify-between">
        {/* Top Portal Nav */}
        <header className="border-b border-white/10 bg-black/30 backdrop-blur-md sticky top-0 z-40">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="h-9 w-9 rounded-xl bg-blue-600 text-white flex items-center justify-center font-black shadow-lg shadow-blue-500/40">
                <Sparkles className="h-5 w-5" />
              </div>
              <div className="flex items-center space-x-2">
                <span className="text-base font-black tracking-tight text-white">
                  CBSE<span className="text-blue-400">PaperGen</span>
                </span>
                <span className="rounded-full bg-blue-500/20 border border-blue-400/30 px-2 py-0.5 text-[10px] font-bold text-blue-300">
                  Educator Portal
                </span>
              </div>
            </div>
            <div className="hidden sm:flex items-center space-x-3 text-xs font-semibold text-slate-300">
              <div className="flex items-center space-x-1.5 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 px-3 py-1 rounded-full">
                <span className="h-2 w-2 rounded-full bg-emerald-400 animate-pulse" />
                <span>Supabase Database Online</span>
              </div>
              <div className="flex items-center space-x-1 text-slate-400">
                <GraduationCap className="h-4 w-4 text-blue-400" />
                <span>Classes 10, 11 & 12</span>
              </div>
            </div>
          </div>
        </header>

        {/* Hero & Login/Signup Grid */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 sm:py-16 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center flex-1">
          {/* Left Column: Platform Showcase */}
          <div className="lg:col-span-6 space-y-6">
            <div className="inline-flex items-center space-x-2 rounded-full bg-blue-500/10 border border-blue-400/20 px-3.5 py-1 text-xs font-semibold text-blue-300">
              <Cpu className="h-3.5 w-3.5 text-blue-400" />
              <span>Autonomous CBSE Curriculum Engine • 2025-2026 Blueprint</span>
            </div>

            <h1 className="text-3xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight">
              CBSE Teacher Portal & Question Paper Studio
            </h1>

            <p className="text-sm sm:text-base text-slate-300 leading-relaxed max-w-xl">
              Create an educator profile or log in below to assemble Board exams, chapter tests, 
              and step-wise marking schemes with embedded vector diagrams and your school crest.
            </p>

            {/* Feature Highlights Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-2">
              <div className="rounded-2xl bg-white/5 border border-white/10 p-4 backdrop-blur-xs">
                <div className="flex items-center space-x-2 text-blue-400 font-bold text-xs mb-1">
                  <Layers className="h-4 w-4" />
                  <span>2,761+ Questions</span>
                </div>
                <p className="text-xs text-slate-300">
                  Pre-loaded CBSE question bank covering Classes 10, 11 & 12 in Math & Science.
                </p>
              </div>

              <div className="rounded-2xl bg-white/5 border border-white/10 p-4 backdrop-blur-xs">
                <div className="flex items-center space-x-2 text-emerald-400 font-bold text-xs mb-1">
                  <FileCheck className="h-4 w-4" />
                  <span>Sections A to E</span>
                </div>
                <p className="text-xs text-slate-300">
                  Strict section breakdown: MCQs, VSA (2M), SA (3M), LA (5M), and Case-Based (4M).
                </p>
              </div>

              <div className="rounded-2xl bg-white/5 border border-white/10 p-4 backdrop-blur-xs">
                <div className="flex items-center space-x-2 text-amber-400 font-bold text-xs mb-1">
                  <ShieldCheck className="h-4 w-4" />
                  <span>Step-Wise Rubrics</span>
                </div>
                <p className="text-xs text-slate-300">
                  Automated marking schemes with fractional mark allocations for accurate grading.
                </p>
              </div>

              <div className="rounded-2xl bg-white/5 border border-white/10 p-4 backdrop-blur-xs">
                <div className="flex items-center space-x-2 text-purple-400 font-bold text-xs mb-1">
                  <Bookmark className="h-4 w-4" />
                  <span>Saved Papers Archive</span>
                </div>
                <p className="text-xs text-slate-300">
                  Your created question papers are saved in Supabase and ready to re-download anytime.
                </p>
              </div>
            </div>

            {/* AI Student Copy Evaluator Feature Callout */}
            <div className="rounded-2xl bg-gradient-to-r from-amber-500/20 via-orange-500/20 to-purple-500/20 border border-amber-400/40 p-4 backdrop-blur-xs flex items-center justify-between gap-3">
              <div>
                <div className="flex items-center space-x-1.5 text-amber-400 font-bold text-xs mb-0.5">
                  <Zap className="h-4 w-4 fill-current" />
                  <span>NEW: AI Student Copy Evaluator</span>
                  <span className="bg-amber-400 text-slate-950 font-black text-[9px] px-1.5 py-0.2 rounded-full">
                    ₹500 / batch
                  </span>
                </div>
                <p className="text-xs text-slate-300">
                  Upload student copies in PDF — AI grades each step using official CBSE marking rubrics!
                </p>
              </div>
              <button
                type="button"
                onClick={() => setIsCopyCheckerOpen(true)}
                className="shrink-0 px-3.5 py-2 rounded-xl bg-amber-400 hover:bg-amber-500 text-slate-950 font-black text-xs shadow-md transition-all flex items-center space-x-1 cursor-pointer"
              >
                <span>Learn More</span>
                <ArrowRight className="h-3.5 w-3.5" />
              </button>
            </div>

            {/* Quick Stats Pill */}
            <div className="flex items-center space-x-6 pt-2 border-t border-white/10 text-xs text-slate-400">
              <div><strong className="text-white font-black text-sm">2,761+</strong> CBSE Items</div>
              <div><strong className="text-white font-black text-sm">3</strong> Grade Levels</div>
              <div><strong className="text-white font-black text-sm">Typst</strong> Vector PDFs</div>
              <div><strong className="text-white font-black text-sm">1-Click</strong> Instant Export</div>
            </div>
          </div>

          {/* Right Column: Teacher Authentication Box */}
          <div className="lg:col-span-6">
            <TeacherAuthModal isModal={false} onAuthenticated={(user) => setTeacherUser(user)} />
          </div>
        </div>

        {/* AI Copy Checker Modal */}
        <AiCopyCheckerModal
          isOpen={isCopyCheckerOpen}
          onClose={() => setIsCopyCheckerOpen(false)}
          currentUser={teacherUser}
        />

        {/* Portal Footer */}
        <footer className="border-t border-white/10 bg-black/40 py-6 text-center text-xs text-slate-400">
          <div className="max-w-7xl mx-auto px-4 space-y-1">
            <p>Autonomous AI Question Paper Generator • Official CBSE Board Blueprint & NCERT Catalog</p>
            <p className="text-slate-500">FastAPI • Next.js 14 • Typst Typesetting • Supabase PostgreSQL</p>
          </div>
        </footer>
      </main>
    );
  }

  // 2. EDUCATOR STUDIO (Shown once teacher logs in)
  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-50 via-white to-slate-50">
      {/* Top Navigation Bar */}
      <nav className="border-b border-slate-200 bg-white/95 backdrop-blur-md sticky top-0 z-40 shadow-xs">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          {/* Logo & Brand */}
          <div className="flex items-center space-x-3 cursor-pointer" onClick={() => setActiveTab('create')}>
            <div className="h-9 w-9 rounded-xl bg-blue-600 text-white flex items-center justify-center font-black shadow-md shadow-blue-500/30">
              <Sparkles className="h-5 w-5" />
            </div>
            <div>
              <span className="text-base font-black tracking-tight text-slate-900">
                CBSE<span className="text-blue-600">PaperGen</span>
              </span>
              <span className="ml-2 inline-flex items-center rounded-full bg-blue-100 px-2 py-0.5 text-[10px] font-bold text-blue-800">
                Pro v1.2
              </span>
            </div>
          </div>

          {/* Center Tab Switcher: Create vs Saved Papers */}
          <div className="flex items-center bg-slate-100 p-1 rounded-xl border border-slate-200 shadow-inner">
            <button
              type="button"
              onClick={() => setActiveTab('create')}
              className={`flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all ${
                activeTab === 'create'
                  ? 'bg-white text-blue-700 shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              <FileText className="h-3.5 w-3.5" />
              <span>Create Question Paper</span>
            </button>
            <button
              type="button"
              onClick={() => setActiveTab('saved')}
              className={`flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all ${
                activeTab === 'saved'
                  ? 'bg-white text-blue-700 shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              <Bookmark className="h-3.5 w-3.5" />
              <span>My Saved Papers</span>
              {typeof teacherPaperCount === 'number' && teacherPaperCount > 0 && (
                <span className="ml-1 rounded-full bg-blue-600 text-white text-[10px] px-1.5 py-0.2">
                  {teacherPaperCount}
                </span>
              )}
            </button>
          </div>

          {/* AI Copy Checker Feature Pill Button */}
          <button
            type="button"
            onClick={() => setIsCopyCheckerOpen(true)}
            className="hidden sm:flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-gradient-to-r from-amber-400 via-orange-400 to-amber-500 hover:from-amber-500 hover:to-orange-500 text-slate-950 font-black text-xs shadow-md shadow-orange-500/20 transition-all cursor-pointer"
            title="Upload student copies to check automatically via AI for ₹500"
          >
            <Zap className="h-3.5 w-3.5 fill-current" />
            <span>AI Copy Checker</span>
            <span className="bg-black/15 text-slate-950 text-[10px] font-black px-1.5 py-0.2 rounded-md">
              ₹500
            </span>
          </button>

          {/* Right Educator Profile & Status */}
          <div className="flex items-center space-x-2.5">
            {teacherUser ? (
              <div className="flex items-center space-x-2 bg-slate-100/90 pl-3 pr-2 py-1.5 rounded-2xl border border-slate-200 shadow-xs">
                <div className="flex flex-col text-left">
                  <div className="flex items-center space-x-1.5">
                    <span className="text-xs font-black text-slate-900 truncate max-w-[120px] sm:max-w-[170px]">
                      {teacherUser.name}
                    </span>
                    {typeof teacherPaperCount === 'number' && (
                      <span className="rounded-full bg-emerald-100 text-emerald-800 text-[9px] font-bold px-1.5 py-0.2" title="Total Papers Created">
                        {teacherPaperCount} {teacherPaperCount === 1 ? 'Paper' : 'Papers'}
                      </span>
                    )}
                  </div>
                  <span className="text-[10px] font-semibold text-slate-500 truncate max-w-[120px] sm:max-w-[170px]">
                    {teacherUser.school}
                  </span>
                </div>
                <button
                  type="button"
                  onClick={handleLogout}
                  title="Sign Out / Switch Profile"
                  className="rounded-lg p-1.5 text-slate-400 hover:bg-slate-200 hover:text-red-600 transition-colors"
                >
                  <LogOut className="h-3.5 w-3.5" />
                </button>
              </div>
            ) : (
              <div className="hidden sm:flex items-center space-x-2.5 text-xs font-semibold text-slate-600">
                <div className="flex items-center space-x-1 text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200">
                  <span className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse" />
                  <span>Typst Print Engine</span>
                </div>
                <div className="flex items-center space-x-1 text-blue-700 bg-blue-50 px-2.5 py-1 rounded-full border border-blue-200">
                  <GraduationCap className="h-3.5 w-3.5" />
                  <span>Classes 10, 11, 12</span>
                </div>
              </div>
            )}
          </div>
        </div>
      </nav>

      {/* Hero Header (only shown on Create Tab) */}
      {activeTab === 'create' && (
        <div className="pt-8 pb-4 text-center px-4">
          <div className="inline-flex items-center space-x-2 rounded-full bg-slate-100 border border-slate-200 px-3.5 py-1 text-xs font-semibold text-slate-700 mb-3">
            <Cpu className="h-3.5 w-3.5 text-blue-600" />
            <span>Official CBSE Blueprint Assembler with Embedded Diagrams & School Branding</span>
          </div>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight max-w-3xl mx-auto">
            Autonomous AI Question Paper Generator
          </h1>
          <p className="mt-2 text-sm sm:text-base text-slate-600 max-w-2xl mx-auto">
            Generate print-ready CBSE Board exams, unit tests, and step-wise marking schemes with LaTeX formulas, 
            embedded circuit and ray diagrams, custom school logos, and Typst compilation.
          </p>
        </div>
      )}

      {/* Main Content Area */}
      {activeTab === 'create' ? (
        <Wizard
          initialExam={loadedExam}
          currentUser={teacherUser}
          onViewSavedPapers={() => setActiveTab('saved')}
        />
      ) : (
        <SavedPapersDashboard
          onLoadExamToPreview={handleLoadExamToPreview}
          onSwitchToGenerator={() => setActiveTab('create')}
        />
      )}

      {/* AI Copy Checker Modal */}
      <AiCopyCheckerModal
        isOpen={isCopyCheckerOpen}
        onClose={() => setIsCopyCheckerOpen(false)}
        currentUser={teacherUser}
      />

      {/* Footer */}
      <footer className="mt-16 border-t border-slate-200 bg-white py-8 text-center text-xs text-slate-500">
        <div className="max-w-7xl mx-auto px-4 space-y-2">
          <p>Autonomous AI Question Paper Generation System • Built with FastAPI, Next.js, Typst & Supabase PostgreSQL</p>
          <p className="text-slate-400">Strictly adheres to official CBSE Board Blueprints & NCERT Textbook Ingestion Catalog.</p>
        </div>
      </footer>
    </main>
  );
}
