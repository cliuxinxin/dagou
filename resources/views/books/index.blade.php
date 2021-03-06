@extends('layouts.app')

@section('content')
    <div class="container">
        <row>
            <h1>共享图书馆</h1>
            <blockquote>
                大家可以把自己的书放上来共享。系统可以帮忙追踪书本的借阅情况。
            </blockquote>
        </row>
        <hr>
        <div class="row">
            <table class="table table-striped">
                <tr>
                    <th>书名</th>
                    <th>拥有者（微信号）</th>
                    <th>介绍</th>
                    <th>借阅</th>
                </tr>
                @foreach($items as $item)
                    <tr>
                        <td><a href="{{ route('bookDetail',$item->id) }}">{{$item->name}}</a></td>
                        <td><a href="{{ route('userBooks',$item->user->id) }}">{{$item->user->profiles->first()->weixin}}</a></td>
                        <td>{{$item->detail}}</td>
                        @if($item->is_lended == 'Y')
                        <td>
                            <div class="row-fluid">
                                <div class="span12">
                                    <span>
                                    {{ $item->lendedDate()->diffForHumans() }}已经被{{ $item->lendedUserName() }}借走
                                    </span>
                                    <span>
                                        @if(Auth::user()&&$item->isOwnedByUser(Auth::user()))
                                            <form method="POST" action="{{ route('lendingRecordUpdate') }}">
                                                {{ csrf_field() }}
                                                <input type="hidden" name="book_id" value="{{ $item->id }}">
                                                <input type="hidden" name="lending_record_id" value="{{ $item->latestLendingRecrod()->id }}">
                                                <button type="submit" class="btn-sm btn-success">确认还书</button>
                                            </form>
                                        @endif
                                    </span>
                                </div>
                            </div>
                        </td>
                        @else
                        <td>
                            @if(!Auth::user())
                                登陆后可以借阅
                            @endif
                            @if(Auth::user()&&!$item->isOwnedByUser(Auth::user()))
                            <form method="POST" action="{{ route('lendingRecordStore') }}">
                                {{ csrf_field() }}
                                <input type="hidden" name="book_id" value="{{ $item->id }}">
                                <button type="submit" class="btn-sm btn-success">借阅</button>
                            </form>
                            @endif
                        </td>
                        @endif
                    </tr>
                @endforeach
            </table>
        </div>
        {{ $items->links() }}
        <hr>
        <div class="row col-md-6">
            <form method="POST" action="{{ route('bookStore') }}">
                {{ csrf_field() }}
                <div class="form-group">
                    <label for="name">书名</label>
                    <input type="text" class="form-control" name="name">
                </div>

                <div class="form-group" >
                    <label for="detail">介绍</label>
                    <textarea rows="3" class="form-control" name="detail"></textarea>
                </div>

                <button type="submit" class="btn btn-success">添加</button>
            </form>
        </div>
    </div>
@endsection
