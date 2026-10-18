'use client';

import React, { useState, useEffect } from 'react';
import Wizard from '../components/Wizard';
import SavedPapersDashboard from '../components/SavedPapersDashboard';
import TeacherAuthModal, { TeacherUser } from '../components/TeacherAuthModal';
import { 
  Sparkles, 
  FileText, 
  GraduationCap, 
  Cpu, 
  Bookmark, 
  UserCheck, 
  LogOut, 
  School,
  ShieldCheck
} from 'lucide-react';

export default function Home() {
  const [activeTab, setActiveTab] = useState<'create' | 'saved'>('create');
  const [loadedExam, setLoadedExam] = useState<any>(null);
  const [teacherUser, setTeacherUser] = useState<TeacherUser | null>(null);
  const [isAuthLoaded, setIsAuthLoaded] = useState(false);

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

  const handleLogout = () => {
    if (confirm('Are you sure you want to log out of this educator profile?')) {
      localStorage.removeItem('cbse_auth_teacher');
      setTeacherUser(null);
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

  return (
    <main className="min-h-screen bg-gradient-to-b from-slate-50 via-white to-slate-50">
      {/* Teacher Authentication Gate (Sign Up / Sign In) */}
      {isAuthLoaded && !teacherUser && (
        <TeacherAuthModal onAuthenticated={(user) => setTeacherUser(user)} />
      )}

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
            </button>
          </div>

          {/* Right Educator Profile & Status */}
          <div className="flex items-center space-x-2.5">
            {teacherUser ? (
              <div className="flex items-center space-x-2 bg-slate-100/90 pl-3 pr-2 py-1.5 rounded-2xl border border-slate-200 shadow-xs">
                <div className="flex flex-col text-left">
                  <span className="text-xs font-black text-slate-900 truncate max-w-[130px] sm:max-w-[180px]">
                    {teacherUser.name}
                  </span>
                  <span className="text-[10px] font-semibold text-slate-500 truncate max-w-[130px] sm:max-w-[180px]">
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
